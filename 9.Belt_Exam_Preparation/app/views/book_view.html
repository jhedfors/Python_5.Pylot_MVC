<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
  <title>Travel Dashboard</title>

  <!-- CSS  -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="/assets/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="/assets/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>

</head>
<body>

   <div class="row">
     <div class="col s6">
      </div>
      <div class="col s6">
          <a href="/books">Home</a>    <a href="/logout">Logout</a>
      </div>
   </div>
   <div class="row">
     <div class="col s6">
       <h3><?php echo $reviews[0]['title'] ?></h3>
       <p>
         Author: <?php echo $reviews[0]['author_name'] ?>
       </p>
       <h4>Reviews</h4>
       <div class="review">
         <?php
         for ($i=0; $i < count($reviews) ; $i++) {
           $review = $reviews[$i];
          ?>
          <h5><a href="/books/<?php echo $review['book_id'] ?>"><?php echo $review['title'] ?></a></h5>
          <p>
            Rating: <?php echo $review['star_rating'] ?> stars
          </p>
          <p>
            <a href="/users/<?php echo $review['user_id'] ?>"><?php echo $review['user_name'] ?></a> says: <?php echo $review['review'] ?>
          </p>
          <p>
            Posted on <?php echo $review['reviewed_on'];
            if ($review['user_id'] == $this->session->userdata('active_id')){
              echo "<a href ='/delete/".$review['review_id']."/".$review['book_id']."/".$review['author_id']."'>Delete this review</a>";
            }

             ?>
          </p>
        <?php
       }
       ?>

       </div>
     </div>
     <div class="col s6">
       <h3>Add a Review:</h3>
       <form class="" action="/main/add_review" method="post">
         <textarea name="review" rows="8" cols="40"></textarea>
         <div class="col s2">
           <label for="star_rating">Rating</label>
         </div>
         <div class="browser-default input-field col s3">
           <select name="star_rating">
             <option value = '1'>1</option>
             <option value = '2'>2</option>
             <option value = '3'>3</option>
             <option value = '4'>4</option>
             <option value = '5'>5</option>
           </select>
         </div>
         <div class="col s2">
            <label>stars</label>
         </div>
         <div class="row">
           <input type="hidden" name="book_id" value="<?php echo $reviews[0]['book_id'] ?>">
          <input type="hidden" name="user_id" value="<?php echo $this->session->userdata('active_id')?>">
           <input type="submit" value="Submit">
         </div>

       </form>
     </div>
   </div>


  <!--  Scripts-->
  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <script src="/assets/js/materialize.js"></script>
  <script src="/assets/js/init.js"></script>
  <script type="text/javascript">
    $(document).ready(function() {
      $('select').material_select();
    });
  </script>
  </body>
</html>
