$(document).ready(()=>{
    let mainOutput = $('#output');
    let subOutput = $('#output2');
    let op = $('#operator');
    let num1 = $('#num1');
    let num2 = $('#num2');
    let temp = $('#temp');
    let clearData = ()=>{
        num1.val('')
        op.val('')
        num2.val('')
        temp.val('')
    };
    let clearOutput = ()=>{
        mainOutput.html('');
        subOutput.html('');
    };
    let digitError = ()=>{
        mainOutput.html(0);
        subOutput.html('Reach Digit Limit');
        temp.val(0);
    };
    $('.btn-default').click(function(e){

        if (('+-*!/').indexOf(mainOutput.html()) != -1){
            mainOutput.html('')
        }
        if ($(this).val() == '.'
            && (mainOutput.html()).indexOf('.') != -1)
            return;
        if (mainOutput.html() == '0'
            || subOutput.html() == 'Reach Digit Limit'){
            clearOutput();
        }
        if(temp.val() !== ''){
            clearOutput();
            clearData();
        }
        clearData();
        mainOutput.html($(this).val());
        subOutput.append($(this).val());
        if(mainOutput.html().length > 12){
            digitError();
        }
    });
    $('#clearButton').click(e=>{
        mainOutput.html('0');
        subOutput.html('');
        clearData();
    });
    $('.btn-equal').click(function (e) {
        e.preventDefault();
        var that = $(this).parent('#output');
        $.getJSON($SCRIPT_ROOT+'/ui_calc',
            {stmt:$('#output2').text()},
            d=>{
                alert('연산결과: '+d.result)
                $(that).html('<span>테스트</span>')

            });
    });

    /*$('.btn-operate').click(function(){
        let newOperator = $(this).val();
        if(num1.val() !== ''
            && ('+-*!/').indexOf(num1.val()) == -1
            && op.val() !== ''){
            num2.val(mainOutput.html());
            if(('+-*!/').indexOf(num2.val()) != -1) return;
            let x = {};
            $.getJSON($SCRIPT_ROOT+'/calc',x,d=>{
                if(d.result.toString().length > 13){
                    digitError();
                }else{
                    // 계산결과
                }
            });

        }
    })*/
});













