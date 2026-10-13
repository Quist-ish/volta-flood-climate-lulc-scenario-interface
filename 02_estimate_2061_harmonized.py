#!/usr/bin/env python3
"""Reimplementation of Supplement S15 for the harmonized CAP500 pathway.

This script does not pretend to be the unavailable original revision execution file.
It reconstructs the described procedure from the supplied CAP500 archive:
(1) midpoint model climatologies; (2) same CHIRPS transfer rules; (3) midpoint
harmonized LULC state with clipping/closure; (4) HGB delta emulator; (5) cellwise
interpolation of dL and dI; (6) reported-regime calculations.
"""
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
ROOT=Path(__file__).resolve().parents[1]
IN=ROOT/'data'/'analysis_ready'/'CAP500_FACTORIAL_PREDICTIONS.csv.gz'
OUT=ROOT/'generated_outputs'; OUT.mkdir(exist_ok=True)
df=pd.read_csv(IN)
CLIM=['PRCPTOT','Rx1day','R10mm','R20mm','SDII']
TOPO=['HAND_m','elevation_m','slope_deg','log_upstream_area']
LULC=['LULC_forest_fraction','LULC_shrub_savanna_grass_fraction','LULC_wetland_fraction','LULC_cropland_fraction','LULC_urban_fraction','LULC_barren_fraction']
FEAT=CLIM+TOPO+LULC; KEY=['climate_model','scenario','period','cell_id']
# Training table for delta emulator
base=df[df.state=='C0L0'][KEY+FEAT+['prob_cap500']].rename(columns={**{c:c+'_base' for c in FEAT},'prob_cap500':'p_base'})
tr=df.merge(base,on=KEY,how='left')
for c in FEAT: tr['delta_'+c]=tr[c]-tr[c+'_base']
XCOLS=FEAT+['delta_'+c for c in FEAT]+['p_base']
y=tr.prob_cap500-tr.p_base
em=HistGradientBoostingRegressor(max_iter=800,learning_rate=0.05,max_leaf_nodes=63,min_samples_leaf=20,random_state=0).fit(tr[XCOLS],y)
# Midpoint states
ix=['climate_model','scenario','cell_id','state']
mid=df[df.period=='mid_2041_2060'].set_index(ix).sort_index(); late=df[df.period=='late_2081_2100'].set_index(ix).sort_index(); assert mid.index.equals(late.index)
new=mid.copy().reset_index(); new['period']='estimated_2061_2080'
for c in CLIM: new[c+'_future_model']=((mid[c+'_future_model']+late[c+'_future_model'])/2).values
for c in LULC:
    v=mid[c].copy(); m=mid.index.get_level_values('state').isin(['C0L1','C1L1']); v.loc[m]=(mid.loc[m,c]+late.loc[m,c])/2; new[c]=v.values
m=new.state.isin(['C0L1','C1L1']); new.loc[m,LULC]=new.loc[m,LULC].clip(0,1); ss=new.loc[m,LULC].sum(axis=1); ids=new.loc[m].index[ss>1]; new.loc[ids,LULC]=new.loc[ids,LULC].div(ss[ss>1],axis=0)
base2=new[new.state=='C0L0'].set_index(['climate_model','scenario','cell_id'])
f=new.state.isin(['C1L0','C1L1']); ids=new.index[f]; keys=pd.MultiIndex.from_frame(new.loc[ids,['climate_model','scenario','cell_id']])
for c in ['PRCPTOT','Rx1day','SDII']:
    new.loc[ids,c]=base2.loc[keys,c].to_numpy()*(new.loc[ids,c+'_future_model'].to_numpy()/new.loc[ids,c+'_hist_model'].to_numpy())
for c in ['R10mm','R20mm']:
    new.loc[ids,c]=np.clip(base2.loc[keys,c].to_numpy()+(new.loc[ids,c+'_future_model'].to_numpy()-new.loc[ids,c+'_hist_model'].to_numpy()),0,214)
# Emulator input
bcols=['climate_model','scenario','cell_id']+FEAT+['prob_cap500']
b=new[new.state=='C0L0'][bcols].rename(columns={**{c:c+'_base' for c in FEAT},'prob_cap500':'p_base'})
nb=new.merge(b,on=['climate_model','scenario','cell_id'],how='left')
for c in FEAT: nb['delta_'+c]=nb[c]-nb[c+'_base']
nb['delta_emulated']=em.predict(nb[XCOLS])
# Interpolate dL/dI from archived direct windows; take dC from emulated C1L0.
pp=df.pivot_table(index=KEY,columns='state',values='prob_cap500')
pp['dL']=pp.C0L1-pp.C0L0; pp['dI']=pp.C1L1-pp.C1L0-pp.C0L1+pp.C0L0
mi=pp.xs('mid_2041_2060',level='period'); la=pp.xs('late_2081_2100',level='period')
est=(mi[['dL','dI']]+la[['dL','dI']])/2
c1=nb[nb.state=='C1L0'].set_index(['climate_model','scenario','cell_id'])
est['dC']=pd.Series(c1.delta_emulated,index=c1.index); est['combined']=est.dC+est.dL+est.dI
area=df[df.state=='C0L0'].drop_duplicates('cell_id').set_index('cell_id').cell_area_km2
q=est.reset_index(); q['area']=q.cell_id.map(area)
model=q.groupby(['climate_model','scenario']).apply(lambda d: pd.Series({k:np.average(d[k],weights=d.area) for k in ['dC','dL','dI','combined']}),include_groups=False)
model.to_csv(OUT/'estimated_2061_CAP500_model_level.csv')
head=model.groupby('scenario').median(); tot=head.dC.abs()+head.dL.abs()+head.dI.abs(); head['climate_share_pct']=head.dC.abs()/tot*100; head['lulc_share_pct']=head.dL.abs()/tot*100; head['interaction_share_pct']=head.dI.abs()/tot*100
head.to_csv(OUT/'estimated_2061_CAP500_basin_headline.csv')
# Create cell-level 2061 experiment for downstream spatial diagnostics.
ens=est.reset_index().groupby(['scenario','cell_id'])[['dC','dL','dI','combined']].median()
rows=[]
for s in ['ssp245','ssp585']:
    sub=nb[(nb.climate_model=='ACCESS-CM2')&(nb.scenario==s)]; c00=sub[sub.state=='C0L0'].set_index('cell_id'); c01=sub[sub.state=='C0L1'].set_index('cell_id'); c10=sub[sub.state=='C1L0'].set_index('cell_id')
    for cid in c00.index:
        r={'scenario':s,'period':'estimated_2061_2080','cell_id':cid,'lon':c00.loc[cid,'lon'],'lat':c00.loc[cid,'lat'],'area':c00.loc[cid,'cell_area_km2']}
        for c in TOPO: r[c]=c00.loc[cid,c]
        for c in CLIM: r[c+'_base']=c00.loc[cid,c]; r['d_'+c]=c10.loc[cid,c]-c00.loc[cid,c]
        for c in LULC:
            short=c.split('_')[1]; r['base_'+short]=c00.loc[cid,c]; r['d_'+short]=c01.loc[cid,c]-c00.loc[cid,c]
        e=ens.loc[(s,cid)]; r.update({'dC':e.dC,'dL':e.dL,'dI':e.dI,'comb':e.combined}); rows.append(r)
T=pd.DataFrame(rows)
for c in ['dC','dL','dI','comb']: T[c]=T[c].round(6)
T['tot']=(T.dC.abs()+T.dL.abs()+T.dI.abs()).round(6); T['w']=T.tot*T.area
T['regime']=np.where(T.tot<0.01,'inactive',np.where((T.dL.abs()+T.dI.abs()).round(6)>=T.dC.abs(),'landscape','climate'))
T.to_csv(OUT/'estimated_2061_cell_experiments.csv',index=False)

# Rebuild the full eight-experiment cell table and S18-style summary.
# Direct-period rows are exact from the supplied CAP500 probabilities; estimated-period rows are from this reimplementation.
K3=['scenario','period','cell_id']
pp0=df.pivot_table(index=KEY,columns='state',values='prob_cap500')
pp0['dC']=pp0.C1L0-pp0.C0L0; pp0['dL']=pp0.C0L1-pp0.C0L0; pp0['dI']=pp0.C1L1-pp0.C1L0-pp0.C0L1+pp0.C0L0; pp0['comb']=pp0.C1L1-pp0.C0L0
a1=df[df.climate_model=='ACCESS-CM2']; d00=a1[a1.state=='C0L0'].set_index(K3); d01=a1[a1.state=='C0L1'].set_index(K3)
TD=d00[['lon','lat','cell_area_km2']+TOPO+CLIM+LULC].copy(); TD.columns=['lon','lat','area']+TOPO+[c+'_base' for c in CLIM]+['base_'+c.split('_')[1] for c in LULC]
for c in LULC: TD['d_'+c.split('_')[1]]=d01[c]-d00[c]
d10m=df[df.state=='C1L0'].set_index(KEY)[CLIM]; d00m=df[df.state=='C0L0'].set_index(KEY)[CLIM]; dcl=(d10m-d00m).groupby(level=K3).median(); dcl.columns=['d_'+c for c in CLIM]
TD=TD.join(dcl).join(pp0.groupby(K3)[['dC','dL','dI','comb']].median()).reset_index()
T8=pd.concat([TD,T],ignore_index=True,sort=False)
for c in ['dC','dL','dI','comb']: T8[c]=T8[c].round(6)
T8['tot']=(T8.dC.abs()+T8.dL.abs()+T8.dI.abs()).round(6); T8['w']=T8.tot*T8.area
T8['regime']=np.where(T8.tot<0.01,'inactive',np.where((T8.dL.abs()+T8.dI.abs()).round(6)>=T8.dC.abs(),'landscape','climate'))
period_order=['near_2021_2040','mid_2041_2060','estimated_2061_2080','late_2081_2100']; labels={'near_2021_2040':'2021–2040','mid_2041_2060':'2041–2060','estimated_2061_2080':'2061–2080*','late_2081_2100':'2081–2100'}
rows=[]
for s in ['ssp245','ssp585']:
  for per in period_order:
    d=T8[(T8.scenario==s)&(T8.period==per)]
    order=np.argsort(-d.w.values); cum=np.cumsum(d.w.values[order])/d.w.sum(); cuma=np.cumsum(d.area.values[order])/d.area.sum()
    A=lambda r:d.loc[d.regime==r,'area'].sum()/d.area.sum()*100
    S=lambda r:d.loc[d.regime==r,'w'].sum()/d.w.sum()*100
    ntg=lambda k:abs((d[k]*d.area).sum())/(d[k].abs()*d.area).sum()
    rows.append({'Scenario':'SSP2-4.5' if s=='ssp245' else 'SSP5-8.5','Period':labels[per],
      'Area clim. (%)':A('climate'),'Area land. (%)':A('landscape'),'Area inact. (%)':A('inactive'),
      'Signal clim. (%)':S('climate'),'Signal land. (%)':S('landscape'),
      'A50 (%)':cuma[cum>=.5][0]*100,'A80 (%)':cuma[cum>=.8][0]*100,
      'NTG dC':ntg('dC'),'NTG dL':ntg('dL'),'Cellwise climate share (%)':(d.dC.abs()*d.area).sum()/d.w.sum()*100})
S18=pd.DataFrame(rows); S18.to_csv(OUT/'spatial_attribution_S18_reimplementation.csv',index=False)
print('2061–2080 CAP500 method reimplementation:')
print(head.round(6).to_string())
print('NOTE: compare with locked current reported tables; exact original revision execution file was not supplied.')
