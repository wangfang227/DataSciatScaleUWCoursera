import os
import pandas as pd
import numpy as np
from nltk.metrics import edit_distance
import seaborn as sns
from IPython.display import Image
import matplotlib.pyplot as plt
#from util import *


# create lon, lat
os.getcwd()
os.chdir('C:\\Users\\usz003g\\Documents\\Coursera\\DataSci_Capstone')

v=pd.read_csv("detroit-blight-violations.csv")
v.columns

v['lat']=[float(x.split('\n')[2].split()[0].strip('(),')) for x in v.ViolationAddress]
v['lon']=[float(x.split('\n')[2].split()[1].strip('(),')) for x in v.ViolationAddress]

v.describe()

c=pd.read_csv("detroit-crime.csv")
c.columns
c.ix[:3,['LAT','LON']]
c.ix[:,['LAT','LON']].isnull().sum()


c['lat']=[float(x) if isinstance(x, (int, float)) and 41<float(x)<43 else 42.40 for x in c.LAT]
c['lon']=[float(x) if isinstance(x, (int, float)) and -84<float(x)<-82 else -83.10 for x in c.LON]

c['lat'].describe()
c['lon'].describe()

p=pd.read_csv("detroit-demolition-permits.csv")
p.columns

p.site_location.loc[pd.isnull(p.site_location)]='(42.40,-83.10)'

'''
float(p.site_location[0].split('\n')[2].split()[1].strip('(),'))
a=x.find('(')+1
b=x.find(')')
x[x.find('(')+1:x.find(')')].split(',')
x='abc'
x=p.site_location[1220]
len(x.split('\n'))
x.split('\n')[2].split()
len(x.split('\n')[2].split())
x.split('\n')[2].split()[0].strip('(),')
lat1=[float(x.split('\n')[2].split()[0].strip('(),'))  if len(x.split('\n')[2].split())>0 else 42 for x in p.site_location[:470]]
lat2=[float(x.split('\n')[2].split()[0].strip('(),'))  if len(x.split('\n')[2].split())>0 else 42 for x in p.site_location[471:]]
'''

p['lat']=[float(x[x.find('(')+1:x.find(')')].split(',')[0]) if x.find('(')!=-1 and x.find(')')!=-1 else 42.40 for x in p.site_location]
p['lon']=[float(x[x.find('(')+1:x.find(')')].split(',')[1]) if x.find('(')!=-1 and x.find(')')!=-1 else -83.10 for x in p.site_location]

#p.lat.ix[p.lat==42.40]=None
#p.lon.ix[p.lon==-83.10]=None

p.lat[1:500]
p.lon[1:500]

p.columns

d=pd.read_csv("detroit-311.csv")

d.describe()
d.lat.describe()
d.lng.describe()
d.lon=d.lng


p.lat.describe()
p.lon.describe()

c.lat.describe()
c.lon.describe()

v.lat.describe()
v.lon.describe()

print(p.shape,
v.shape,
c.shape,
d.shape)

############# Create addr

v.columns
v['addr']=[x.split('\n')[0] for x in v.ViolationAddress]
v.addr
v['addr'].isnull().sum()

c.columns
c['addr']=c.ADDRESS

p.columns
p['addr'] = p['SITE_ADDRESS']

d.columns
d['addr']=d['address']

#clean the address
def addr_clean(s0):
    s=str(s0).lower()
    s=s.replace(',', ' ')
    s=s.replace('street', 'st')
    s=s.replace('road', 'rd')
    s=s.replace('avenue', 'av')
    s=s.replace('drive', 'd')
    s=s.replace('boulevard', 'bd')
    s=s.replace('blvd', 'bd')
    s=s.replace('detroit',' ')
    s=s.replace('michigan', ' ')
    s=s.replace('detroit',' ')
    s=s.replace('mi', ' ')
    s=s.replace('west','w')
    s=s.replace('east','e')
    s=s.replace('north','n')
    s=s.replace('south','s')
    s=s.strip(' \t\n\r')
    s=s.rstrip()
    s=s.lstrip()
    return s
    #print(s)
    
#add_clean('20089 Vaughan WEST STREET Detroit , Michigan')
v['addr'].isnull()
v['addr']=v['addr'].map(addr_clean)
v['addr']

p['addr'].isnull()
p['addr']=p['addr'].map(addr_clean)
p['addr']

c['addr'].isnull()
c['addr']=c['addr'].map(addr_clean)
c['addr']

d['addr'].isnull()
d['addr']=d['addr'].map(addr_clean)
d['addr']



#####################  plot the crime data  #########################

r=6

p.lat=p.lat.round(r)
p.lon=p.lon.round(r)

v.lat=v.lat.round(r)
v.lon=v.lon.round(r)

c['lat']=c.lat.round(r)
c['lon']=c.lon.round(r)

d['lat']=d.lat.round(r)
d['lon']=d.lng.round(r)

p[pd.notnull(p.lat)]

#permit with crime
#pc=pd.DataFrame()
#pc=pd.merge(p[pd.notnull(p.lat)],c,how='outer',on=['lat','lon'])


#bt=pd.merge(p.loc[:,['lat','lon','addr']], c.loc[:,['lat','lon','addr']],how='outer',on=['lat','lon'])
#bt=pd.merge(bt, v.loc[:,['lat','lon','addr']],how='outer',on=['lat','lon'])
#bt=pd.merge(bt, d.loc[:,['lat','lon','addr']],how='outer',on=['lat','lon'])



#concatenate the data frames 

p.shape

len(p)


p['id']=range(p.shape[0])
c['id']=range(p.shape[0], p.shape[0]+c.shape[0])
v['id']=range(p.shape[0]+c.shape[0], p.shape[0]+c.shape[0]+v.shape[0])
d['id']=range(p.shape[0]+c.shape[0]+v.shape[0], p.shape[0]+c.shape[0]+v.shape[0]+d.shape[0])

'''
bt=pd.concat((p.loc[:,['id','lat','lon','addr']],c.loc[:,['lat','lon','addr']]), axis=0,ignore_index=True)
bt=pd.concat((bt,v.loc[:,['id','lat','lon','addr']),axis=0,ignore_index=True)
bt=pd.concat((bt,d.loc[:,['id','lat','lon','addr']]),axis=0,ignore_index=True)
'''

bt=pd.concat((p,c), axis=0,ignore_index=True)
bt=pd.concat((bt,v),axis=0,ignore_index=True)
bt=pd.concat((bt,d),axis=0,ignore_index=True)

sum(p['id'].isnull())

bt.shape
bt.loc[bt['id'].isnull(),]

sum(bt.groupby('id')['id'].transform('count')>=2)
#good, every id is unique
sum(bt['id'].value_counts()>1)

bt.head(40)

bt=bt[['id','lat','lon','addr']]

bt.shape
p.shape
v.shape
c.shape
d.shape

p.to_csv('permit.csv',index=False,encoding = 'utf8')
v.to_csv('violation.csv',index=False,encoding = 'utf8')
c.to_csv('crime.csv',index=False,encoding = 'utf8')
d.to_csv('d311.csv',index=False,encoding = 'utf8')

#delete the wrong address

#use the median to impute the wrong lat lon

bt['lat']=[float(x) if isinstance(x, (int, float)) and 41<float(x)<43 else 42.40 for x in bt.lat]
bt['lon']=[float(x) if isinstance(x, (int, float)) and -84<float(x)<-82 else -83.10 for x in bt.lon]

bt.lat.describe()
bt.lon.describe()

bt=bt.sort((['addr','lon','lat']))

######### address exact match cluster

def exact_match(bt):
    count=0
    table={}
    cluster=[]
    for a in bt.addr:
       if a in table: 
           cluster.append(count)
       else: 
           count+=1
           bt['cluster']=count
           table[a]=count
           cluster.append(count)
    bt['cluster']=np.array(cluster)
    return table, count

addr_dict, addr_count=exact_match(bt)

addr_dict, addr_count

######### address fuzzy match 
def fuzzy_match(x,y):
    x_list=x.split()
    y_list=y.split()
    x_set=set(x_list)
    y_set=set(y_list)
    start_number=(x_list[0].isdigit() and y_list[0].isdigit())
    if start_number:
        #print(x_list[0], y_list[0])
        num_flag=(x_list[0]==y_list[0])
    else: num_flag=False
    com_flag=len(x_set & y_set)>=1
    dis_flag=(edit_distance(x,y)<5)
    #print(start_number,num_flag,com_flag,dis_flag)
    if start_number:
        if num_flag and com_flag and dis_flag:
            return True
    else:
        if com_flag and dis_flag:
            return True
    return False
    
fuzzy_match('5035  balfour','5297  balfour')    
    
fuzzy_match('balfour st','5297  balfour st')    

fuzzy_match('balfour st','\\balfour st')    

############# use fuzzy match for the addresses in the same cluster

bt.iloc[0,:]

clusters=bt['cluster'].unique()
len(bt['cluster'].unique())
bt.shape

### bt never changed concatenated file 

#b=pd.DataFrame(bt.drop_duplicates('cluster'))
#shouldn't drop duplicates, otherwise the c v d information can't be merged in

b=bt
b.shape

sum(b['addr'].isnull())
b.ix[b['addr']=='',]
#drop the addr blank row
b=b.ix[b['addr']!='',]
b.shape

bt.head(20)
#nc=b.shape[0]

sum(b['id'].isnull())


def refine_clusters(df):
    clusters = {}
    
    row0 = df.iloc[0, :]
    prev_cluster = row0['cluster']
    prev_addr = row0['addr']
    row0_id =row0['id']
    clusters[row0_id] = prev_cluster

    for index, row in df.iterrows():
        addr = row['addr']
        cluster = row['cluster']
        id = row['id']
        
        if id == row0_id:
            continue
        
        if cluster != prev_cluster:
            if fuzzy_match(addr, prev_addr):
                cluster = prev_cluster
            else:
                prev_cluster = cluster
                prev_addr = addr
        
        clusters[id] = cluster
    
    df['refined_cluster'] = df['id'].map(lambda x: clusters[x])
    return df

b.iterrows()

b2=refine_clusters(b)

b2.columns
b2.shape
b2.ix[b2['cluster']!=b2['refined_cluster'],:]
#48218 rows got combined into a similar cluster

b2.shape
b.shape

len(b2.refined_cluster.unique())
len(b2.cluster.unique())

b.columns

'''
def cluster_match(b):
    addr0=b.ix[0,'addr']
    clus0=b.ix[0,'cluster']
    prev_addr=addr0
    prev_clus=clus0
    nc=b.shape[0]
    for i in range(nc):
        #print(i,prev_addr,prev_clus)
        if i==0:
            continue
        curr_addr=b.ix[i,'addr']
        curr_clus=b.ix[i,'cluster']
        if curr_clus!=prev_clus:
            if fuzzy_match(prev_addr,curr_addr):
                print('matched',i,prev_addr,prev_clus,curr_addr,curr_clus)
                curr_clus=prev_clus
                curr_addr=prev_addr                
            else:
                prev_addr=curr_addr
                prev_clus=curr_clus
           
#cluster_match(b[:2000])
#cluster_match doesn't work

'''

#b2.to_csv('all_addr.csv',index=False,encoding = 'utf8')



###############################################################################
################################# starting from here ##########################

################################# Establish buildings #########################
import os
import pandas as pd
import numpy as np
from nltk.metrics import edit_distance
import seaborn as sns
#from IPython.display import Image

#from util import *

os.getcwd()
os.chdir('C:\\Users\\usz003g\\Documents\\Coursera\\DataSci_Capstone')

b2=pd.read_csv('all_addr.csv',encoding='utf-8',index_col=False)

b2.shape

b2 = b2.ix[(b2['lat'] > 42) & (b2['lat'] < 43),:]
b2 = b2.ix[(b2['lon'] > -84) & (b2['lon'] < -82),:]

b2.shape

sum(b2['lat'].isnull())
sum(b2['lon'].isnull())

len(b2['refined_cluster'].unique())

#all the lon lat has been imputed to the median value, no missing any more

#b2['lat']=[float(x) if isinstance(x, (int, float)) and 41<float(x)<43 else 42.40 for x in b2.lat]
#b2['lon']=[float(x) if isinstance(x, (int, float)) and -84<float(x)<-82 else -83.10 for x in b2.lon]

# first clusted by address, if lat lon missing, the buildings can still be clustered by address

# further cluster by lat lon

b2['addr_len']=[len(x) for x in b2['addr']]

#sum(b2['refined_addr'].isnull())
#b2=b2.ix[b2['addr_len']>=5]

b2=b2.drop(b2.ix[(b2['lat']==42.400000) & (b2['lon']==-83.100000) & (b2['addr_len']<5),:].index,axis=0)
b2.shape

# good, no lat lon imputed and address not valid case 

# if address length <5, cluster by lat lon 

addrwrong=b2.ix[(b2['addr_len']<10),:]

addrwrong['lat']=round(addrwrong['lat'],4)
addrwrong['lon']=round(addrwrong['lon'],4)

addrwrong.sort(['lat','lon','addr'])

nr=addrwrong.shape[0]

addrwrong.index=range(nr)

len(addrwrong['refined_cluster'].unique())

addrwrong.shape

for i in range(nr):
    if i==0:
        continue
    i0=i-1
    lat0=addrwrong.loc[i0,'lat']
    lon0=addrwrong.ix[i0,'lon']
    refined_cluster0=addrwrong.ix[i0,'refined_cluster']
    
    lat=addrwrong.ix[i,'lat']
    lon=addrwrong.ix[i,'lon']
    refined_cluster=addrwrong.ix[i,'refined_cluster']
    
    if lat==lat0 and lon==lon0:
        addrwrong.ix[i,'refined_cluster']=refined_cluster0
        
len(addrwrong['refined_cluster'].unique())       

#cleaned only two addresses
    
#merge the further refined cluster into b2

b3=b2.ix[b2['addr_len']>=10,:]

b3.shape

b2.shape

addrwrong.shape

b2=pd.concat([b3,addrwrong],axis=0)
    
#establish building
b2.shape

b2=b2.sort('refined_cluster')


'''
top_right=b2.groupby('refined_cluster').agg({'lat':max,'lon':max}).reset_index()
bottom_left=b2.groupby('refined_cluster').agg({'lat':min,'lon':min}).reset_index()

top_right.columns=['refined_cluster', 'tright_lon', 'tright_lat']
bottom_left.columns=['refined_cluster', 'bleft_lon', 'bleft_lat']
   
    
b2=pd.merge(b2,top_right,how='left',on='refined_cluster')
b2=pd.merge(b2,bottom_left,how='left',on='refined_cluster')

b2.shape
'''



### plot this cleaned address data
import matplotlib
#from mpl_toolkits.basemap import Basemap

'''
import folium
map1 = folium.Map(location=[42.38, -83.12])
lat_t=round(b2.lat[0],2)
lon_t=round(b2.lon[0],2)
map1.add_children([lat_t,lon_t])
map_osm.create_map(path='osm.html')
'''

#import geoplotlib

#data=b2.loc[pd.notnull(b2.lat) & pd.notnull(b2.lon),['lat','lon']]

b2.lat.describe()
b2.lon.describe()

'''
geoplotlib.dot(data,point_size=0.8)
geoplotlib.show()
geoplotlib.savefig('violation')
'''

# delete the outliers 

b2.shape

sns.lmplot('lon', 'lat', data=b2, fit_reg=False, size=10)
#Image('detroit_area.png')
    
#plot each file 
    
#p v c d: (7133, 59) (307804, 35) (119931, 21) (19680, 18)


#permit

import geoplotlib

b3=b2.ix[b2['id']<7133,:]
sns.lmplot('lon', 'lat', data=b3, fit_reg=False, size=10)
#Image('detroit_area.png')


geoplotlib.dot(b3,point_size=0.8)
geoplotlib.show()

#crime

b3=b2.ix[(b2['id']>=7133) & (b2['id']<7133+307804),:]
sns.lmplot('lon', 'lat', data=b3, fit_reg=False, size=10)
#Image('detroit_area.png')


geoplotlib.dot(b3,point_size=0.8)
geoplotlib.show()
#Image('crime.png')
plt.savefig('crime.png')    

#violation

b3=b2.ix[(7133+307804<=b2['id']) & (b2['id']<7133+307804+119931),:]
sns.lmplot('lon', 'lat', data=b3, fit_reg=False, size=10)
#Image('detroit_area.png')
     
geoplotlib.dot(b3,point_size=0.8)
geoplotlib.show()
    
    
#311
      
b3=b2.ix[(7133+307804+119931<=b2['id']) & (b2['id']<7133+307804+119931+19680),:]
sns.lmplot('lon', 'lat', data=b3, fit_reg=False, size=10)
#Image('detroit_area.png')
      
geoplotlib.dot(b3,point_size=0.8)
geoplotlib.show()

########################## modeling part #########################################
######################### create traing and test data ####################################


p=pd.read_csv('permit.csv',encoding='utf-8')
v=pd.read_csv('violation.csv',encoding = 'utf8')
c=pd.read_csv('crime.csv',encoding = 'utf8')
d=pd.read_csv('d311.csv',encoding = 'utf8')

p.columns
p.head(10)

#permit with violation
'''
pv=pd.DataFrame()
pv=pd.merge(p[pd.notnull(p.lat)],v,how='left',on=['lat','lon'])
p.describe()
v.describe()
pv.describe()
pv.shape
'''

b2.columns
p.columns

#x=b2[]

p['BLD_PERMIT_TYPE'].value_counts()


b3=pd.merge(p.ix[pd.notnull(p.lat) & pd.notnull(p.lon),['id','BLD_PERMIT_TYPE']],b2,how='right',on=['id'])
b3.shape
b3['BLD_PERMIT_TYPE']=b3['BLD_PERMIT_TYPE'].fillna('nondism')

b3.ix[b3['BLD_PERMIT_TYPE']=='nondism','y']=0
b3.ix[b3['BLD_PERMIT_TYPE']!='nondism','y']=1
b3['y'].value_counts()

b3['BLD_PERMIT_TYPE'].value_counts()

b3=b3.drop(['BLD_PERMIT_TYPE'],axis=1)

b3.columns

b3.shape

#b3.to_csv('building.csv',index=False,encoding = 'utf8')
b3.columns

#train.to_csv('train.csv',index=False,encoding = 'utf8')
#test.to_csv('test.csv',index=False,encoding = 'utf8')



####################################### merge in other predictors #####

#train=pd.read_csv('train.csv',encoding = 'utf8')
#test=pd.read_csv('test.csv',encoding = 'utf8')

b=pd.read_csv('building.csv',encoding = 'utf8')
p=pd.read_csv('permit.csv',encoding='utf-8')
v=pd.read_csv('violation.csv',encoding = 'utf8')
c=pd.read_csv('crime.csv',encoding = 'utf8')
d=pd.read_csv('d311.csv',encoding = 'utf8')

b.shape

p.columns 

b.columns

b['y'].value_counts()

p.shape

p['BLD_PERMIT_TYPE'].value_counts()

# get variables from v c d 
v.columns
c.columns
d.columns

### violation variables
'JudgmentAmt' 'ViolationCategory' 'PaymentStatus' 'ViolationCode'

v['ViolationCode'].value_counts()
v['ViolDescription'].value_counts()
v['FineAmt'].value_counts()
v['JudgmentAmt'].value_counts()
v['PaymentStatus'].value_counts()
v['ViolationCategory'].value_counts()


v.columns

def test_var(v):
    return(v.value_counts(),
    v.describe(),
    sum(v.isnull()==True))

print(test_var(v['ViolationCode']))
print(test_var(v['ViolDescription']))
print(test_var(v['FineAmt']))
print(test_var(v['JudgmentAmt']))
print(test_var(v['PaymentStatus']))
print(test_var(v['ViolationCategory']))

v1=v.ix[:,['ViolationCode','ViolDescription','FineAmt','JudgmentAmt','PaymentStatus','ViolationCategory']]
for i in range(v1.shape[1]):
   print(v1.iloc[:,i].value_counts(), sum(v1.iloc[:,i].isnull()))


#### crime data
c.columns
c[c.columns[0]].value_counts()

c1=c.ix[:,['CATEGORY',	'OFFENSEDESCRIPTION','STATEOFFENSEFILECLASS',	'INCIDENTDATE','HOUR','SCA','PRECINCT','COUNCIL']]
for i in range(c1.shape[1]):
   print(c1.iloc[:,i].value_counts(), sum(c1.iloc[:,i].isnull()))



### 311 data
d.columns
d1=d.ix[:,['issue_type', 'ticket_status', 'issue_description','rating']]
for i in range(d1.shape[1]):
   print(d1.iloc[:,i].value_counts(), sum(d1.iloc[:,i].isnull()))



#start merging 

b.columns

v.columns

#b=pd.DataFrame(b.drop_duplicates('refined_cluster'))
b.shape

#not using the text varaible now 'ViolDescription''OFFENSEDESCRIPTION','issue_description',

t=pd.merge(b, v.ix[:,['id', 'ViolationCode','FineAmt','JudgmentAmt','PaymentStatus','ViolationCategory']],how='left',on=['id'])
t=pd.merge(t, c.ix[:,['id','CATEGORY',	'STATEOFFENSEFILECLASS','HOUR','SCA','PRECINCT','COUNCIL']],how='left',on=['id'])
t=pd.merge(t, d.ix[:,['id','issue_type', 'ticket_status', 'rating']],how='left',on=['id'])

del(b,v,c,d)

#b.shape
t.shape

len(t.refined_cluster.unique())

# to build the X matrix, the p records must be excluded
#t['id']>=7133

#if I don't exclude cases from permit, I have to delete the _999 variables 

t.columns
tx=t.ix[:,['refined_cluster','ViolationCode', 'FineAmt', 'JudgmentAmt',
       'PaymentStatus', 'ViolationCategory', 'CATEGORY',
       'STATEOFFENSEFILECLASS','HOUR', 'SCA', 'PRECINCT',
       'COUNCIL', 'issue_type', 'ticket_status',
       'rating']]
     
for i in range(tx.shape[1]):
   #print(tx.columns[i],sum(tx.iloc[:,i].isnull()),tx.iloc[:,i].value_counts())
   print(tx.iloc[:,i].value_counts())
   
tx.shape
   
tx.HOUR.value_counts()
tx.rating.value_counts()

#clean amount
def clean_amt(v):
    v=float(str(v).strip('$'))
    return v
    
tx.FineAmt=tx.FineAmt.map(clean_amt)

tx.JudgmentAmt=tx.JudgmentAmt.map(clean_amt)

tx.columns

#for amount, fill missing as 0

tx[['FineAmt', 'JudgmentAmt','rating']]=tx[['FineAmt', 'JudgmentAmt','rating']].fillna(0)

tx[['ViolationCode', 'PaymentStatus',
       'ViolationCategory', 'CATEGORY', 'STATEOFFENSEFILECLASS',
        'SCA', 'PRECINCT', 'COUNCIL', 'issue_type',
       'ticket_status','HOUR']]=tx[['ViolationCode', 'PaymentStatus',
       'ViolationCategory', 'CATEGORY', 'STATEOFFENSEFILECLASS',
       'SCA', 'PRECINCT', 'COUNCIL', 'issue_type',
       'ticket_status','HOUR']].fillna('999')


tx.columns
tx.shape


import pandas as pd

#del(dummies)

dummies = pd.get_dummies(tx[['PaymentStatus',
       'ViolationCategory', 'STATEOFFENSEFILECLASS',
       'PRECINCT', 'COUNCIL', 'issue_type',
       'ticket_status']])
       
dummies.shape

dummies.columns


'''
var999=dummies.columns[dummies.columns.str.endswith('999')]
dummies=dummies.drop(list(var999),axis=1)
dummies.columns
X_dummy=dummies.groupby('refined_cluster').sum().reset_index()
X_contin=tx.groupby('refined_cluster').sum('FineAmt', 'JudgmentAmt','rating')
'''

X=pd.concat([tx.ix[:,['refined_cluster','FineAmt', 'JudgmentAmt','rating']],dummies],axis=1)
X['refined_cluster']
X.shape

X=X.groupby(['refined_cluster']).sum().reset_index()
X.shape


# the reason why my model has a higher accuray is simply because I have used 999 category, weird
var999=X.columns[X.columns.str.endswith('999')]
X=X.drop(list(var999),axis=1)
X.columns
#test 
X.columns[X.columns.str.endswith('999')]


y = t.groupby('refined_cluster').agg({'y':max}).reset_index()
y.shape

y.sum(axis=0)

#y.value_counts()

#random sample from Y=0 cases as negative buildings

xy=pd.merge(X,y,how='outer',on=['refined_cluster'])
xy.shape

#xy=xy.fillna(0)

del(t,tx)

#xy.to_csv('building full xy.csv',index=False)


blight=xy.ix[xy.y==1,:]
nblight0=xy.ix[xy.y==0,:]

from sklearn.cross_validation import train_test_split
nblight,dropped = train_test_split(nblight0, test_size=0.96, random_state=107)

nblight.shape

blight.shape

X1=pd.concat([blight,nblight],axis=0).drop(['refined_cluster','y'],axis=1)
X1.shape
X1.columns

Y1=pd.DataFrame(pd.concat([blight.y,nblight.y],axis=0))
Y1.shape
Y1.columns

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.30, random_state=107)

x_train.shape
y_train.shape

x_test.shape
y_test.shape

train=pd.concat([y_train,x_train],axis=1)
test=pd.concat([y_test,x_test],axis=1)

#from sklearn.metrics import matthews_corrcoef

#X_train

#check the correlations 
from sklearn.feature_selection import SelectKBest, chi2

select_chi2=50
ch2 = SelectKBest(chi2, k=select_chi2)
X_train = ch2.fit_transform(x_train, y_train)
X_train.shape
y_train.shape

X_test = ch2.transform(x_test)
X_test.shape
y_test.shape

'''
pd.DataFrame(X_train).to_csv('X_train.csv',index=False)
pd.DataFrame(y_train).to_csv('y_train.csv',index=False)

pd.DataFrame(X_test).to_csv('X_test.csv',index=False)
pd.DataFrame(y_test).to_csv('y_test.csv',index=False)
'''

#X_train=pd.DataFrame(X_train)

#selected columns
x_train.columns[ch2.get_support()]

#pearsonr(X_train,y_train)[0]


'''
top_ranked_features = sorted(enumerate(ch2.scores_),key=lambda x:x[1], reverse=True)[:1000]
top_ranked_features_indices = map(list,zip(*top_ranked_features))[0]
for feature_pvalue in zip(np.asarray(train_vectorizer.get_feature_names())[top_ranked_features_indices],ch2.pvalues_[top_ranked_features_indices]):
        print(feature_pvalue)
  '''      

#from scipy.stats import pearsonr

#from sklearn.metrics import matthews_corrcoef
#for i in range(X_train.shape[1]):
#    pearsonr(np.array(y_train), np.array(X_train[i]))[0]



###################### rank the variables using random forest importance ###########################
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split

clf = RandomForestClassifier(n_estimators=100)

clf.fit(X_train, y_train)

X_train.shape
X_test.shape

feat_imp = pd.Series(clf.feature_importances_, index=x_train.columns[ch2.get_support()])
feat_imp.sort_values(inplace=True, ascending=False)
feat_imp.head(20).plot(kind='barh', title='Feature importance')
feat_imp.head(20).plot(kind='bar', title='Feature Rank')


plt.figure()
plt.title("Feature importances")
plt.bar(range(X_train.shape[1]),feat_imp,
       color="r", align="center")
locs, labels = plt.xticks(range(X_train.shape[1]),x_train.columns[ch2.get_support()])
plt.setp(labels, rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.show()


#sum(clf.predict(X_test) == y_test) / float(len(y_test))
'''
clf.predict(x_test)[:,None].shape
np.array(y_test).shape

from __future__ import division

y_test_p=clf.predict(X_test)
y_test_p.tolist()[-30:]
y_test[-30:]
'''
#float(sum(sum(clf.predict(X_test)== np.array(y_test).T)))/ float(len(y_test))

### create the count variables ###

#accuracy using the test data
float(sum(sum(clf.predict(X_test)== np.array(y_test).T)))/ float(len(y_test))

float(sum(sum(clf.predict(X_train)== np.array(y_train).T)))/ float(len(y_train))


x_train.columns[ch2.get_support()]

#p-value the small the better
sorted(ch2.pvalues_)[19]

x_train.columns[ch2.pvalues_<sorted(ch2.pvalues_,reverse=1)[19]]

pvalues=np.vstack([x_train.columns,ch2.pvalues_])

np.sort(pvalues)[:20]


x_train.columns[ch2.get_support()]

clf.predict(X_test)[-5:]
#float(sum(sum(clf.predict(x_train)== np.array(y_train).T)))/ float(len(y_train))

from sklearn.metrics import roc_curve, roc_auc_score
pred_probs = clf.predict_proba(X_test)[:, 1]
round(roc_auc_score(y_test, pred_probs), 5)

fpr, tpr, thresholds = roc_curve(y_test, pred_probs, pos_label=1)
plt.figure(figsize=(6, 6), dpi=200)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='RF')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc='best')
plt.show()









#plot the tree
fig, ax = plt.subplots(figsize=(40, 40))
#clf.plot_tree(clf, num_trees=0, ax=ax)

import pydotplus
from sklearn import tree
from sklearn.externals.six import StringIO

#import pydotplus

clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
clf.predict(X_test)

with open("detroit.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
    
import os
os.unlink('detroit.dot')

dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("detroit.pdf") 

tree

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")


from IPython.display import Image  
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=x_train.columns[ch2.get_support()],  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  
