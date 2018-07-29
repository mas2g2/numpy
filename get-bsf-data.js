var exec = require('child_process').exec;
var child;
array = process.argv.slice(2)
var cmdArgs = ""
var twoArrays = 0;
for(i = 0; i < array.length; i++){
        cmdArgs += array[i] + " "
        if(array[i] == '/')twoArrays = 1;
}
//console.log(array)
//executes command 'pwd'

child = exec("python3 numpy/bsf.py "+cmdArgs,function (error, stdout, stderr){
        var result = "Statistics data:"
        console.log('stdout : '+stdout);
        var linearRegression = stdout.substring(
                stdout.lastIndexOf("Linear Regression :") ,
                stdout.lastIndexOf(",\nF")
        );
        var firstArrayData = stdout.substring(
                stdout.lastIndexOf("First Array :") ,
                stdout.lastIndexOf(",\nS")
        );
        var secondArrayData = stdout.substring(
                stdout.lastIndexOf("Second Array :") ,
                stdout.lastIndexOf("\n")
        );
        var statAn = stdout.substring(
                stdout.lastIndexOf("Statistical Analysis :") ,
                stdout.lastIndexOf("\n")
        );
        statAn = statAn.replace("Statistical Analysis :","")
        console.log('stderr : '+stderr);
	if(twoArrays == 1){
                console.log("Linear Regression : "+linearRegression);
                console.log("First Array : "+firstArrayData);
                console.log("Second Array : "+secondArrayData);
        }
        else{
                console.log(statAn);
        }
        if(error != null){
                console.log('exec error : '+error);
        }
});