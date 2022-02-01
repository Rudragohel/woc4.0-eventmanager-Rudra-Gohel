const evalution ={
0:'0',
1: '-0.03',
2: '0.0',
3: '-0.07',
4: '0.12',
5: '0.1',
6: '0.05',
7: '0.0',
8: '0.09',
9: '0.12',
10: '0.06',
11: '-0.3',
12: '-0.4',
13: '-0.83',
14: '0.09',
15: '-0.74',
16: '-0.58',
17: '-1.05',
18: '-0.72',
19: '-0.87',
20: '-0.65',
21: '-0.55',
22: '-0.67',
23: '-0.57',
24: '-0.64',
25: '-1.02',
26: '-0.96',
27: '-1.87',
28: '-0.95',
29: '-0.96',
30: '-0.92',
31: '-1.1',
32: '-0.7',
33: '-0.54',
34: '5.51',
35: '-0.31',
36: '9.37',
37: '9.28',
38: '9.05',
39: '7.23',
40: '7.83',
41: '7.46',
42: '7.75',
43: '7.61',
44: '7.46',
45: '7.75',
46: '7.76',
47: '7.54',
48: '7.76',
49: '7.76',
50: '9.15',
51: '9.17',
52: '9.3',
53: '9.23',
54: '9.3',
55: '9.38',
56: '9.46',
57: '9.8',
58: '9.69',
59: '9.15',
60: '9.76',
61: '8.74',
62: '8.92',
63: '9.12',
64: '9.53',
65: '9.74',
66: '11.42',
67: '11.53',
68: '12.1',
69: '57.63',
70: 'M14',
71: '11.66',
72: '62.13',
73: '58.12',
74: '58.12',
75: '55.85',
76: '55.85',
77: '55.85',
78: 'M1',
79: '!!CheckMate:  White Wins !!',
}
total_moves=79
var move=0;

function next_move(){
    if(move<total_moves){
        move++;
        document.getElementById("display_image").src=move.toString()+".svg";
        if(move==total_moves){
            document.getElementById("display_evalution").innerHTML=evalution[move];
        }
        else{
            document.getElementById("display_evalution").innerHTML="Evaluation: " +evalution[move];
        }
        
    }
}

function prev_move(){
    if(move>0){
        move--;
        document.getElementById("display_image").src=move.toString()+".svg";
        document.getElementById("display_evalution").innerHTML="Evaluation: " + evalution[move];
    }
}

