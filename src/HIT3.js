<!-- You must include this JavaScript file -->
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<!-- For the full list of available Crowd HTML Elements and their input/output documentation,
      please refer to https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html -->

<!-- You must include crowd-form so that your task submits answers to MTurk -->
<crowd-form answer-format="flatten-objects">
<script type="text/javascript">
    document.write("<p>The following is a ${type} piece that you need to find the best matching to.</p>")
</script>
<div style="padding:20px;">
  <img width="20%" src="${input}"/> </p>
</div>

 <p> Select 3 pieces that best matches the piece above.</p>
 <p> If the picture is not a clothes or inappropriate, please check the report box. </p>

 <style>
    /* Three image containers (use 25% for four, and 50% for two, etc) */
    .column {
      float: left;
      width: 18.00%;
      padding: 10px;
    }
    
    /* Clear floats after image containers */
    .row::after {
      content: "";
      clear: both;
      display: table;
    }
    
    img{
    max-width:250px;
    max-height:500px;
    }
 </style>

<div class="row">
  <div class="column">
    <img src="${link1}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link1">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link1_report">report</crowd-checkbox>
  </div>
  <div class="column">
    <img src="${link2}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link2">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link2_report">report</crowd-checkbox>
  </div>
  <div class="column">
    <img src="${link3}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link3">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link3_report">report</crowd-checkbox>
  </div>
    <div class="column">
    <img src="${link4}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link4">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link4_report">report</crowd-checkbox>
  </div>
    <div class="column">
    <img src="${link5}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link5">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link5_report">report</crowd-checkbox>
  </div>
</div>
<p></p></br>
<div class="row">
  <div class="column">
    <img src="${link6}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link6">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link6_report">report</crowd-checkbox>
  </div>
  <div class="column">
    <img src="${link7}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link7">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link7_report">report</crowd-checkbox>
  </div>
  <div class="column">
    <img src="${link8}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link8">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link8_report">report</crowd-checkbox>
  </div>
    <div class="column">
    <img src="${link9}" style="width:100%">
    <crowd-checkbox style="padding-left:10px;" name="link9">select</crowd-checkbox> 
    <crowd-checkbox style="padding-left:70px;" name="link9_report">report</crowd-checkbox>
  </div>
</div>

<p></p></br>

</crowd-form>