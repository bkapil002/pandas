import pandas as pd

data ={
    'name' : [
        'brahm' , 'kapila' ,'ram' , 'krishen'
    ],
    'age':[
        12 , 13 , 15 , 48 
    ],
    'father':[
        'ramesh' , 'ramesh' ,'ramesh' , 'ramesh'
    ]
}

df = pd.DataFrame(data)
print(df)