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

