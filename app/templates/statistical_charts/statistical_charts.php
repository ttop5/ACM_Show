{% extends 'base.html' %}

{% block title %}Acm Show{% endblock %}

{% block page %}

<?php
//hours
        $file = 'shell_data/hours/1.txt';
        $H1 = file_get_contents($file);
        $file = 'shell_data/hours/2.txt';
        $H2 = file_get_contents($file);
        $file = 'shell_data/hours/3.txt';
        $H3 = file_get_contents($file);
        $file = 'shell_data/hours/4.txt';
        $H4 = file_get_contents($file);
        $file = 'shell_data/hours/5.txt';
        $H5 = file_get_contents($file);
        $file = 'shell_data/hours/6.txt';
        $H6 = file_get_contents($file);
        $file = 'shell_data/hours/7.txt';
        $H7 = file_get_contents($file);
        $file = 'shell_data/hours/8.txt';
        $H8 = file_get_contents($file);
        $file = 'shell_data/hours/9.txt';
        $H9 = file_get_contents($file);
        $file = 'shell_data/hours/10.txt';
        $H10 = file_get_contents($file);
        $file = 'shell_data/hours/11.txt';
        $H11 = file_get_contents($file);
        $file = 'shell_data/hours/12.txt';
        $H12 = file_get_contents($file);
        $file = 'shell_data/hours/13.txt';
        $H13 = file_get_contents($file);
        $file = 'shell_data/hours/14.txt';
        $H14 = file_get_contents($file);
        $file = 'shell_data/hours/15.txt';
        $H15 = file_get_contents($file);
        $file = 'shell_data/hours/16.txt';
        $H16 = file_get_contents($file);
        $file = 'shell_data/hours/17.txt';
        $H17 = file_get_contents($file);
        $file = 'shell_data/hours/18.txt';
        $H18 = file_get_contents($file);
        $file = 'shell_data/hours/19.txt';
        $H19 = file_get_contents($file);
        $file = 'shell_data/hours/20.txt';
        $H20 = file_get_contents($file);
        $file = 'shell_data/hours/21.txt';
        $H21 = file_get_contents($file);
        $file = 'shell_data/hours/22.txt';
        $H22 = file_get_contents($file);
        $file = 'shell_data/hours/23.txt';
        $H23 = file_get_contents($file);
        $file = 'shell_data/hours/24.txt';
        $H24 = file_get_contents($file);
//days
        $file = 'shell_data/days/1.txt';
        $D1 = file_get_contents($file);
        $file = 'shell_data/days/2.txt';
        $D2 = file_get_contents($file);
        $file = 'shell_data/days/3.txt';
        $D3 = file_get_contents($file);
        $file = 'shell_data/days/4.txt';
        $D4 = file_get_contents($file);
        $file = 'shell_data/days/5.txt';
        $D5 = file_get_contents($file);
        $file = 'shell_data/days/6.txt';
        $D6 = file_get_contents($file);
        $file = 'shell_data/days/7.txt';
        $D7 = file_get_contents($file);
        $file = 'shell_data/days/8.txt';
        $D8 = file_get_contents($file);
        $file = 'shell_data/days/9.txt';
        $D9 = file_get_contents($file);
        $file = 'shell_data/days/10.txt';
        $D10 = file_get_contents($file);
        $file = 'shell_data/days/11.txt';
        $D11 = file_get_contents($file);
        $file = 'shell_data/days/12.txt';
        $D12 = file_get_contents($file);
        $file = 'shell_data/days/13.txt';
        $D13 = file_get_contents($file);
        $file = 'shell_data/days/14.txt';
        $D14 = file_get_contents($file);
        $file = 'shell_data/days/15.txt';
        $D15 = file_get_contents($file);
        $file = 'shell_data/days/16.txt';
        $D16 = file_get_contents($file);
        $file = 'shell_data/days/17.txt';
        $D17 = file_get_contents($file);
        $file = 'shell_data/days/18.txt';
        $D18 = file_get_contents($file);
        $file = 'shell_data/days/19.txt';
        $D19 = file_get_contents($file);
        $file = 'shell_data/days/20.txt';
        $D20 = file_get_contents($file);
        $file = 'shell_data/days/21.txt';
        $D21 = file_get_contents($file);
        $file = 'shell_data/days/22.txt';
        $D22 = file_get_contents($file);
        $file = 'shell_data/days/23.txt';
        $D23 = file_get_contents($file);
        $file = 'shell_data/days/24.txt';
        $D24 = file_get_contents($file);
        $file = 'shell_data/days/25.txt';
        $D25 = file_get_contents($file);
        $file = 'shell_data/days/26.txt';
        $D26 = file_get_contents($file);
        $file = 'shell_data/days/27.txt';
        $D27 = file_get_contents($file);
        $file = 'shell_data/days/28.txt';
        $D28 = file_get_contents($file);
        $file = 'shell_data/days/29.txt';
        $D29 = file_get_contents($file);
        $file = 'shell_data/days/30.txt';
        $D30 = file_get_contents($file);
//months
        $file = 'shell_data/months/1.txt';
        $M1 = file_get_contents($file);
        $file = 'shell_data/months/2.txt';
        $M2 = file_get_contents($file);
        $file = 'shell_data/months/3.txt';
        $M3 = file_get_contents($file);
        $file = 'shell_data/months/4.txt';
        $M4 = file_get_contents($file);
        $file = 'shell_data/months/5.txt';
        $M5 = file_get_contents($file);
        $file = 'shell_data/months/6.txt';
        $M6 = file_get_contents($file);
        $file = 'shell_data/months/7.txt';
        $M7 = file_get_contents($file);
        $file = 'shell_data/months/8.txt';
        $M8 = file_get_contents($file);
        $file = 'shell_data/months/9.txt';
        $M9 = file_get_contents($file);
        $file = 'shell_data/months/10.txt';
        $M10 = file_get_contents($file);
        $file = 'shell_data/months/11.txt';
        $M11 = file_get_contents($file);
        $file = 'shell_data/months/12.txt';
        $M12 = file_get_contents($file);
?>

<script type="text/javascript">
 //hours
        var h1 = <?php if (($H2-$H1) < "0" or ($H2-$H1) > "10000") {echo 0;} else {echo ($H2-$H1);} ?>;
        var h2 = <?php if (($H3-$H2) < "0" or ($H3-$H2) > "10000") {echo 0;} else {echo ($H3-$H2);} ?>;
        var h3 = <?php if (($H4-$H3) < "0" or ($H4-$H3) > "10000") {echo 0;} else {echo ($H4-$H3);} ?>;
        var h4 = <?php if (($H5-$H4) < "0" or ($H5-$H4) > "10000") {echo 0;} else {echo ($H5-$H4);} ?>;
        var h5 = <?php if (($H6-$H5) < "0" or ($H6-$H5) > "10000") {echo 0;} else {echo ($H6-$H5);} ?>;
        var h6 = <?php if (($H7-$H6) < "0" or ($H7-$H6) > "10000") {echo 0;} else {echo ($H7-$H6);} ?>;
        var h7 = <?php if (($H8-$H7) < "0" or ($H8-$H7) > "10000") {echo 0;} else {echo ($H8-$H7);} ?>;
        var h8 = <?php if (($H9-$H8) < "0" or ($H9-$H8) > "10000") {echo 0;} else {echo ($H9-$H8);} ?>;
        var h9 = <?php if (($H10-$H9) < "0" or ($H10-$H9) > "10000") {echo 0;} else {echo ($H10-$H9);} ?>;
        var h10 = <?php if (($H11-$H10) < "0" or ($H11-$H10) > "10000") {echo 0;} else {echo ($H11-$H10);} ?>;
        var h11 = <?php if (($H12-$H11) < "0" or ($H12-$H11) > "10000") {echo 0;} else {echo ($H12-$H11);} ?>;
        var h12 = <?php if (($H13-$H12) < "0" or ($H13-$H12) > "10000") {echo 0;} else {echo ($H13-$H12);} ?>;
        var h13 = <?php if (($H14-$H13) < "0" or ($H14-$H13) > "10000") {echo 0;} else {echo ($H14-$H13);} ?>;
        var h14 = <?php if (($H15-$H14) < "0" or ($H15-$H14) > "10000") {echo 0;} else {echo ($H15-$H14);} ?>;
        var h15 = <?php if (($H16-$H15) < "0" or ($H16-$H15) > "10000") {echo 0;} else {echo ($H16-$H15);} ?>;
        var h16 = <?php if (($H17-$H16) < "0" or ($H17-$H16) > "10000") {echo 0;} else {echo ($H17-$H16);} ?>;
        var h17 = <?php if (($H18-$H17) < "0" or ($H18-$H17) > "10000") {echo 0;} else {echo ($H18-$H17);} ?>;
        var h18 = <?php if (($H19-$H18) < "0" or ($H19-$H18) > "10000") {echo 0;} else {echo ($H19-$H18);} ?>;
        var h19 = <?php if (($H20-$H19) < "0" or ($H20-$H19) > "10000") {echo 0;} else {echo ($H20-$H19);} ?>;
        var h20 = <?php if (($H21-$H20) < "0" or ($H21-$H20) > "10000") {echo 0;} else {echo ($H21-$H20);} ?>;
        var h21 = <?php if (($H22-$H21) < "0" or ($H22-$H21) > "10000") {echo 0;} else {echo ($H22-$H21);} ?>;
        var h22 = <?php if (($H23-$H22) < "0" or ($H23-$H22) > "10000") {echo 0;} else {echo ($H23-$H22);} ?>;
        var h23 = <?php if (($H24-$H23) < "0" or ($H24-$H23) > "10000") {echo 0;} else {echo ($H24-$H23);} ?>;
        var h24 = <?php if (($H1-$H24) < "0" or ($H1-$H24) > "10000") {echo 0;} else {echo ($H1-$H24);} ?>;
//days
        var d1 = <?php if (($D2-$D1) < "0" or ($D2-$D1) > "100000") {echo 0;} else {echo ($D2-$D1);} ?>;
        var d2 = <?php if (($D3-$D2) < "0" or ($D3-$D2) > "100000") {echo 0;} else {echo ($D3-$D2);} ?>;
        var d3 = <?php if (($D4-$D3) < "0" or ($D4-$D3) > "100000") {echo 0;} else {echo ($D4-$D3);} ?>;
        var d4 = <?php if (($D5-$D4) < "0" or ($D5-$D4) > "100000") {echo 0;} else {echo ($D5-$D4);} ?>;
        var d5 = <?php if (($D6-$D5) < "0" or ($D6-$D5) > "100000") {echo 0;} else {echo ($D6-$D5);} ?>;
        var d6 = <?php if (($D7-$D6) < "0" or ($D7-$D6) > "100000") {echo 0;} else {echo ($D7-$D6);} ?>;
        var d7 = <?php if (($D8-$D7) < "0" or ($D8-$D7) > "100000") {echo 0;} else {echo ($D8-$D7);} ?>;
        var d8 = <?php if (($D9-$D8) < "0" or ($D9-$D8) > "100000") {echo 0;} else {echo ($D9-$D8);} ?>;
        var d9 = <?php if (($D10-$D9) < "0" or ($D10-$D9) > "100000") {echo 0;} else {echo ($D10-$D9);} ?>;
        var d10 = <?php if (($D11-$D10) < "0" or ($D11-$D10) > "100000") {echo 0;} else {echo ($D11-$D10);} ?>;
        var d11 = <?php if (($D12-$D11) < "0" or ($D12-$D11) > "100000") {echo 0;} else {echo ($D12-$D11);} ?>;
        var d12 = <?php if (($D13-$D12) < "0" or ($D13-$D12) > "100000") {echo 0;} else {echo ($D13-$D12);} ?>;
        var d13 = <?php if (($D14-$D13) < "0" or ($D14-$D13) > "100000") {echo 0;} else {echo ($D14-$D13);} ?>;
        var d14 = <?php if (($D15-$D14) < "0" or ($D15-$D14) > "100000") {echo 0;} else {echo ($D15-$D14);} ?>;
        var d15 = <?php if (($D16-$D15) < "0" or ($D16-$D15) > "100000") {echo 0;} else {echo ($D16-$D15);} ?>;
        var d16 = <?php if (($D17-$D16) < "0" or ($D17-$D16) > "100000") {echo 0;} else {echo ($D17-$D16);} ?>;
        var d17 = <?php if (($D18-$D17) < "0" or ($D18-$D17) > "100000") {echo 0;} else {echo ($D18-$D17);} ?>;
        var d18 = <?php if (($D19-$D18) < "0" or ($D19-$D18) > "100000") {echo 0;} else {echo ($D19-$D18);} ?>;
        var d19 = <?php if (($D20-$D19) < "0" or ($D20-$D19) > "100000") {echo 0;} else {echo ($D20-$D19);} ?>;
        var d20 = <?php if (($D21-$D20) < "0" or ($D21-$D20) > "100000") {echo 0;} else {echo ($D21-$D20);} ?>;
        var d21 = <?php if (($D22-$D21) < "0" or ($D22-$D21) > "100000") {echo 0;} else {echo ($D22-$D21);} ?>;
        var d22 = <?php if (($D23-$D22) < "0" or ($D23-$D22) > "100000") {echo 0;} else {echo ($D23-$D22);} ?>;
        var d23 = <?php if (($D24-$D23) < "0" or ($D24-$D23) > "100000") {echo 0;} else {echo ($D24-$D23);} ?>;
        var d24 = <?php if (($D25-$D24) < "0" or ($D25-$D24) > "100000") {echo 0;} else {echo ($D25-$D24);} ?>;
        var d25 = <?php if (($D26-$D25) < "0" or ($D26-$D25) > "100000") {echo 0;} else {echo ($D26-$D25);} ?>;
        var d26 = <?php if (($D27-$D26) < "0" or ($D27-$D26) > "100000") {echo 0;} else {echo ($D27-$D26);} ?>;
        var d27 = <?php if (($D28-$D27) < "0" or ($D28-$D27) > "100000") {echo 0;} else {echo ($D28-$D27);} ?>;
        var d28 = <?php if (($D29-$D28) < "0" or ($D29-$D28) > "100000") {echo 0;} else {echo ($D29-$D28);} ?>;
        var d29 = <?php if (($D30-$D29) < "0" or ($D30-$D29) > "100000") {echo 0;} else {echo ($D30-$D29);} ?>;
        var d30 = <?php if (($D1-$D30) < "0" or ($D1-$D30) > "100000") {echo 0;} else {echo ($D1-$D30);} ?>;

//months
        var m1 = <?php if (($M1-$M12) < "0" or ($M1-$M12) > "500000") {echo 0;} else {echo ($M1-$M12);} ?>;
        var m2 = <?php if (($M2-$M1) < "0" or ($M2-$M1) > "500000") {echo 0;} else {echo ($M2-$M1);} ?>;
        var m3 = <?php if (($M3-$M2) < "0" or ($M3-$M2) > "500000") {echo 0;} else {echo ($M3-$M2);} ?>;
        var m4 = <?php if (($M4-$M3) < "0" or ($M4-$M3) > "500000") {echo 0;} else {echo ($M4-$M3);} ?>;
        var m5 = <?php if (($M5-$M4) < "0" or ($M5-$M4) > "500000") {echo 0;} else {echo ($M5-$M4);} ?>;
        var m6 = <?php if (($M6-$M5) < "0" or ($M6-$M5) > "500000") {echo 0;} else {echo ($M6-$M5);} ?>;
        var m7 = <?php if (($M7-$M6) < "0" or ($M7-$M6) > "500000") {echo 0;} else {echo ($M7-$M6);} ?>;
        var m8 = <?php if (($M8-$M7) < "0" or ($M8-$M7) > "500000") {echo 0;} else {echo ($M8-$M7);} ?>;
        var m9 = <?php if (($M9-$M8) < "0" or ($M9-$M8) > "500000") {echo 0;} else {echo ($M9-$M8);} ?>;
        var m10 = <?php if (($M10-$M9) < "0" or ($M10-$M9) > "500000") {echo 0;} else {echo ($M10-$M9);} ?>;
        var m11 = <?php if (($M11-$M10) < "0" or ($M11-$M10) > "500000") {echo 0;} else {echo ($M11-$M10);} ?>;
        var m12 = <?php if (($M12-$M11) < "0" or ($M12-$M11) > "500000") {echo 0;} else {echo ($M12-$M11);} ?>;

        var data1 = [[1, h1], [2, h2], [3, h3], [4, h4], [5, h5], [6, h6], [7, h7], [8, h8], [9, h9], [10, h10], [11, h11], [12, h12], [13, h13], [14, h14], [15, h15], [16, h16], [17, h17], [18, h18], [19, h19], [20, h20], [21, h21], [22, h22], [23, h23], [24, h24]];
        var data2 = [[1, d1], [2, d2], [3, d3], [4, d4], [5, d5], [6, d6], [7, d7], [8, d8], [9, d9], [10, d10], [11, d11], [12, d12], [13, d13], [14, d14], [15, d15], [16, d16], [17, d17], [18, d18], [19, d19], [20, d20], [21, d21], [22, d22], [23, d23], [24, d24], [25, d25], [26, d26], [27, d27], [28, d28], [29, d29], [30, d30]];
        var data3 = [[1, m1], [2, m2], [3, m3], [4, m4], [5, m5], [6, m6], [7, m7], [8, m8], [9, m9], [10, m10], [11, m11], [12, m12]];
        var dataset1 = [
        {label: "In Last 24 Hours", data: data1},
        ];
        var dataset2 = [
        {label: "In Last 30 Days", data: data2},
        ];
        var dataset3 = [
        {label: "In Last 12 Months", data: data3},
        ];

        var options = {
            series: {
                lines: {
                    show: true ,
                    fill: true,
                    fillColor: { colors: [{ opacity: 0.7 }, { opacity: 0.1}] }
                },
                points: {
                    radius: 3,
                    show: true
                }
            }
        };

        $(document).ready(function () {
            $.plot($("#flot-placeholder1"), dataset1, options);
        });
         $(document).ready(function () {
            $.plot($("#flot-placeholder2"), dataset2, options);
        });
          $(document).ready(function () {
            $.plot($("#flot-placeholder3"), dataset3, options);
        });
</script>

<script>
    $("#mytab a").click(function(e){
        $(this).tab("show");
    })
</script>


<div class="container-fluid">
    <div class="jumbotron">
        <p>In Last 24 Hours</p>
    </div>
</div>

<div id="flot-placeholder1"></div>

<div class="container-fluid">
    <div class="jumbotron">
        <p>In Last 30 Days</p>
    </div>
</div>

<div id="flot-placeholder2"></div>

<div class="container-fluid">
    <div class="jumbotron">
        <p>In Last 12 Months</p>
    </div>
</div>

<div id="flot-placeholder3"></div>

{% endblock %}