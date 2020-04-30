
<style>
  @import '../assets/styles.css';
</style>

<template>
    <div>
      <div class="title">
      <h1>Welcome to Your Student Life Portal!</h1>
    </div>
      <div>
          <b-carousel
            class="carousel-1"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
          >
            <b-carousel-slide class="slide" img-src="img/homepage/carousel1.jpg"></b-carousel-slide>
            <b-carousel-slide class="slide" img-src="img/homepage/carousel2.jpg"></b-carousel-slide>
            <b-carousel-slide class="slide" img-src="img/homepage/carousel3.jpg"></b-carousel-slide>
            <b-carousel-slide class="slide" img-src="img/homepage/carousel4.jpg"></b-carousel-slide>
            <b-carousel-slide class="slide" img-src="img/homepage/carousel5.jpg"></b-carousel-slide>
            <b-carousel-slide class="slide" img-src="img/homepage/carousel6.jpg"></b-carousel-slide>
            <b-carousel-slide class="slide" img-src="img/homepage/carousel7.jpg"></b-carousel-slide>
          </b-carousel>
        </div>

        <!--Sharebook card-->
        <b-container class = "card-holder">
        <b-row>
        <b-col>
            <b-card
              title="Sharebook"
              img-src="img/homepage/sharebook1.jpg"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                Don't break the bank buying textbooks. Share textbooks with like-minded students.
              </b-card-text>

              <b-button class="card-btn" @click="$emit('change-page', 'sharebook')" variant="primary">View Posts</b-button>
            </b-card>
          </b-col>

          <!--Happy Hour card-->
          <b-col>
              <b-card
                title="Happy Hour Finder"
                img-src="img/homepage/happy-hour1.jpg"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
              >
                <b-card-text>
                  Grab a drink and relax after a hard day of studying. Find cheap food and drinks near you.
                </b-card-text>
                <b-button class="card-btn" @click="$emit('change-page', 'happyHours')" variant="primary">View Posts</b-button>
              </b-card>
            </b-col>

            <!--Discount card-->
            <b-col>
                <b-card
                  title="Student Discounts"
                  img-src="img/homepage/student-discount2.jpg"
                  img-alt="Image"
                  img-top
                  tag="article"
                  style="max-width: 20rem;"
                  class="mb-2"
                >
                  <b-card-text>
                    Find local stores that offer student discounts near you. Save money on groceries, clothes etc.
                  </b-card-text>

                  <b-button class="card-btn" @click="$emit('change-page', 'discounts')" variant="primary">View Posts</b-button>
                </b-card>
              </b-col>
            </b-row>
          </b-container>
    </div>
</template>

<script>
      export default {

    }
</script>
