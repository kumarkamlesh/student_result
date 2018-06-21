
    <script>
   function myFunction(){
        var element = document.getElementById("semester");
        var getvalue = element.options[element.selectedIndex].value;
        if(getvalue == "<--Select semester-->")
        {
        var subselect = document.getElementById("first_subject");
        subselect.options.length = 0;
        var supersubselect = document.getElementById("second_subject");
        supersubselect.options.length = 0;
        var supersubselect = document.getElementById("third_subject");
        supersubselect.options.length = 0;
        var supersubselect = document.getElementById("forth_subject");
        supersubselect.options.length = 0;
        var supersubselect = document.getElementById("fifth_subject");
        supersubselect.options.length = 0;
        var supersubselect = document.getElementById("six_subject");
        supersubselect.options.length = 0;
        }

        else if(getvalue == "MCA"){
        var subselect = document.getElementById("subcategory");
                 subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            <!--var optionelement3 = document.createElement("option");-->
            var text = document.createTextNode("<--Select Branch-->");
            var text1 = document.createTextNode("MCA");
            var text2 = document.createTextNode("BTECH");
            <!--var text3 = document.createTextNode("Post Graduates");-->
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            <!--optionelement3.appendChild(text3);-->
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            <!--subselect.appendChild(optionelement3);-->
            document.getElementById("first_subject").style.visibility="visible";
        }
//        else if(getvalue == "BTECH"){
//            var subselect = document.getElementById("subcategory");
//            subselect.options.length = 0;
//            var optionelement = document.createElement("option");
//            var optionelement1 = document.createElement("option");
//            var optionelement2 = document.createElement("option");
//            var optionelement3 = document.createElement("option");
//            var optionelement4 = document.createElement("option");
//            var optionelement5 = document.createElement("option");
//            var optionelement6 = document.createElement("option");
//            var text = document.createTextNode("<--Select-->");
//            var text1 = document.createTextNode("CSE");
//            var text2 = document.createTextNode("ME");
//            var text3 = document.createTextNode("CHE");
//            var text4 = document.createTextNode("CIVIL");
//            var text5= document.createTextNode("ECE");
//            var text6= document.createTextNode("DC");
//            optionelement.appendChild(text);
//            optionelement1.appendChild(text1);
//            optionelement2.appendChild(text2);
//            optionelement3.appendChild(text3);
//            optionelement4.appendChild(text4);
//            optionelement5.appendChild(text5);
//            optionelement6.appendChild(text6);
//            subselect.appendChild(optionelement);
//            subselect.appendChild(optionelement1);
//            subselect.appendChild(optionelement2);
//            subselect.appendChild(optionelement3);
//            subselect.appendChild(optionelement4);
//            subselect.appendChild(optionelement5);
//            subselect.appendChild(optionelement6);
//        }
//

    }
    function subFunction(){
        var elementtop = document.getElementById("first_subject");
        var getvalue = elementtop.options[elementtop.selectedIndex].value;
        if(getvalue == "<--Select-->"){
        var supersubselect = document.getElementById("subcategory1");
        supersubselect.options.length = 0;
        }
       else if(getvalue == "MCA"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
        }
         else if(getvalue == "CSE"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var optionelement6 = document.createElement("option");
            var optionelement7 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            var text6= document.createTextNode("VIIth sem");
            var text7= document.createTextNode("VIIIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            optionelement6.appendChild(text5);
            optionelement7.appendChild(text5);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
            subselect.appendChild(optionelement6);
            subselect.appendChild(optionelement7);
        }
        else if(getvalue == "ME"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var optionelement6 = document.createElement("option");
            var optionelement7 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            var text6= document.createTextNode("VIIth sem");
            var text7= document.createTextNode("VIIIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            optionelement6.appendChild(text6);
            optionelement7.appendChild(text7);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
            subselect.appendChild(optionelement6);
            subselect.appendChild(optionelement7);
        }
        else if(getvalue == "CHE"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var optionelement6 = document.createElement("option");
            var optionelement7 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            var text6= document.createTextNode("VIIth sem");
            var text7= document.createTextNode("VIIIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            optionelement5.appendChild(text6);
            optionelement5.appendChild(text7);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
            subselect.appendChild(optionelement6);
            subselect.appendChild(optionelement7);
        }
        else if(getvalue == "CIVIL"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var optionelement6 = document.createElement("option");
            var optionelement7 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            var text6= document.createTextNode("VIIth sem");
            var text7= document.createTextNode("VIIIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            optionelement6.appendChild(text6);
            optionelement7.appendChild(text7);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
            subselect.appendChild(optionelement6);
            subselect.appendChild(optionelement7);
        }
        else if(getvalue == "ECE"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var optionelement6 = document.createElement("option");
            var optionelement7 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            var text6= document.createTextNode("VIIth sem");
            var text7= document.createTextNode("VIIIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            optionelement6.appendChild(text6);
            optionelement7.appendChild(text7);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
            subselect.appendChild(optionelement6);
            subselect.appendChild(optionelement7);
        }
        else if(getvalue == "DC"){
            var subselect = document.getElementById("subcategory1");
            subselect.options.length = 0;
            var optionelement = document.createElement("option");
            var optionelement1 = document.createElement("option");
            var optionelement2 = document.createElement("option");
            var optionelement3 = document.createElement("option");
            var optionelement4 = document.createElement("option");
            var optionelement5 = document.createElement("option");
            var optionelement6 = document.createElement("option");
            var optionelement7 = document.createElement("option");
            var text = document.createTextNode("Ist sem");
            var text1 = document.createTextNode("IInd sem");
            var text2 = document.createTextNode("IIIrd sem");
            var text3 = document.createTextNode("IVth sem");
            var text4= document.createTextNode("Vth sem");
            var text5= document.createTextNode("VIth sem");
            var text6= document.createTextNode("VIIth sem");
            var text7= document.createTextNode("VIIIth sem");
            optionelement.appendChild(text);
            optionelement1.appendChild(text1);
            optionelement2.appendChild(text2);
            optionelement3.appendChild(text3);
            optionelement4.appendChild(text4);
            optionelement5.appendChild(text5);
            optionelement6.appendChild(text6);
            optionelement7.appendChild(text7);
            subselect.appendChild(optionelement);
            subselect.appendChild(optionelement1);
            subselect.appendChild(optionelement2);
            subselect.appendChild(optionelement3);
            subselect.appendChild(optionelement4);
            subselect.appendChild(optionelement5);
            subselect.appendChild(optionelement6);
            subselect.appendChild(optionelement7);
        }

    }






    </script>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#"> <img src="{%static 'result/images/icon.png'%}" style="width:30px"/>
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="{%url 'homeurl:home'%}">Home <span class="sr-only"></span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{%url 'homeurl:about_us'%}">About us</a>
            </li>

            <li class="nav-item">
                <a class="nav-link disabled" href="#"></a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="{%url 'homeurl:contact_us'%}">Contact us</a>
            </li>

        </ul>
        <ul class="navbar-nav mr-right">
            <li class="nav-item active">

                <a class="nav-link" href="{% url 'homeurl:logout'%}" style="color:white;"><img
                        src="{%static 'result/images/logout.png'%}"
                        style="width:20px"/>Logout <span
                        class="sr-only"></span></a>
            </li>
        </ul>

    </div>
</nav>
<div class="jumbotron-flued">
    <div align="center">
        <div class="box">
            <div class="card" style="width:100%">
                <div class="bg-dark text-white card-header">
                    <h3 style="text-align:center"><i>VIEW RESULT HERE...</i></h3>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <form method="get" enctype="multipart/form-data">
                        {%csrf_token%}
                        <div class="container">
                            <section class="row">
                                <div class="col-sm-6">
                                    <h5 style="color:#7e4781;">Choose Course</h5>


                                    <select name="Category" id="optionMenu" onchange="myFunction()" required="">
                                        <option value="Select"><--Select Course--></option>
                                        <option value="MCA">MCA</option>
                                        <option value="BTECH">BTECH</option>

                                    </select>

                                    <br>
                                    <br>
                                    <h5 style="color:#7e4781;">Choose Branch</h5>
                                    <select name="subcategory" id="subcategory" onchange="subFunction()" required="">

                                    </select>
                                    <br>
                                    <br>
                                    <h5 style="color:#7e4781;">Choose Semester</h5>
                                    <select name="subcategory1" id="subcategory1" required="">

                                  </select>
