<link href="https://s3.amazonaws.com/mturk-public/bs30/css/bootstrap.min.css" rel="stylesheet" /><!-- HIT template: ModerationOfAnImage-v3.0 --><!-- Bootstrap v3.0.3 --><!-- Please note that Bootstrap CSS/JS and JQuery are 3rd party libraries that may update their url/code at any time. Amazon Mechanical Turk (MTurk) is including these libraries as a default option for you, but is not responsible for any changes to the external libraries -->
<link crossorigin="anonymous" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" integrity="sha384-IS73LIqjtYesmURkDE9MXKbXqYA8rvKEp/ghicjem7Vc3mGRdQRptJSz60tvrB6+" rel="stylesheet" />
<!-- You must include this JavaScript file -->
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<!-- For the full list of available Crowd HTML Elements and their input/output documentation,
      please refer to https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html -->

<!-- You must include crowd-form so that your task submits answers to MTurk -->
<div class="col-xs-12 col-md-12"><!-- Instructions -->
<div class="panel-body" id="instructionBody">
<p>Choose 4 top colors that goes well with the given color.</p>

<ul>
    <li>We are specifically looking for best matching colors for clothes</li>
</ul>

</div>
</div>
<style>
    .choice{
        padding: 10px;
        padding-right:50px;
        display: flex;
        width:10%;
        display: table;
        float:left;
    }
    .input-color {
    position: relative;
   }
   .answer {
       padding:30px;
   }

.color-box {
    width: 70px;
    height: 70px;
    display: inline-block;
    outline-style: solid;
    outline-width: thin;
    left: 5px;
    top: 5px;
}

.target-color {
    width: 150px;
    height: 150px;
    display: inline-block;
    padding-left:30px;
    outline-style: solid;
    outline-width: thin;
    left: 5px;
    top: 5px;
    margin-left: 100px;
}

    .row::after {
      content: "";
      clear: both;
      display: table;
    }
    
</style>





    <!-- The crowd-classifier element will create a tool for the Worker to select the
           correct answer to your question.

          Your image file URLs will be substituted for the "image_url" variable below 
          when you publish a batch with a CSV input file containing multiple image file URLs.
          To preview the element with an example image, try setting the src attribute to
          "https://s3.amazonaws.com/cv-demo-images/two-birds.jpg" -->
    <crowd-form answer-format="flatten-objects">
        

<div class="target-color" style="background-color:${target-color};"> </div>
<div class="answer">
    <p style="font-size:20px;"> Choose <b> FOUR </b> colors that go well with the given color above </p>
    <div class="row" style="width:100%;">
        <div class="choice"> <div class="color-box" style="background-color:${color1};"> <crowd-checkbox name="color1"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color2};"> <crowd-checkbox name="color2"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color3};"> <crowd-checkbox name="color3"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color4};"> <crowd-checkbox name="color4"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color5};"> <crowd-checkbox name="color5"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color6};"> <crowd-checkbox name="color6"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color7};"> <crowd-checkbox name="color7"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color8};"> <crowd-checkbox name="color8"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style="background-color:${color9};"> <crowd-checkbox name="color9"></crowd-checkbox></div></div>

        
        
    </div>
    
        <div class="row" style="width:100%;">
        <div class="choice"> <div class="color-box" style= 'background-color: ${color10};'> <crowd-checkbox name="color10"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color11};'> <crowd-checkbox name="color11"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color12};'> <crowd-checkbox name="color12"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color13};'> <crowd-checkbox name="color13"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color14};'> <crowd-checkbox name="color14"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color15};'> <crowd-checkbox name="color15"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color16};'> <crowd-checkbox name="color16"></crowd-checkbox></div></div>
        <div class="choice"> <div class="color-box" style= 'background-color: ${color17};'> <crowd-checkbox name="color17"></crowd-checkbox></div></div>
        
    </div>


</crowd-form>