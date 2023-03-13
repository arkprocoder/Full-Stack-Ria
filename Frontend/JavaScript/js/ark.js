const job = ()=>{
    let Job=true;
    let Fulltime=true;
    let Halftime=true;
    let freelancer=false;
    let salary=50000;
    if(Job && Fulltime && salary>salary){
        console.info("Good Track  0 Backup")
    }
    else if(Job && Halftime && salary<salary){
        console.warn("Full Risk 0 Backup")
    }
    else if(Job && Fulltime && Halftime || freelancer && salary>salary){
        console.warn("Happy Life with 1 Backup")
    }
    else if(Job && Fulltime && Halftime && !freelancer && salary>salary+salary){
        console.log("Hardwork Baby So No Risk with 2 Backups")
    }
    else{
        console.error("A Step toward Poverty");
    }
}
job();