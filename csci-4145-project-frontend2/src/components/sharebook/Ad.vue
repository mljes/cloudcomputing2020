<template>
    <div>
        <!-- ad -->
        <div class="d-flex">
            <!-- image -->
            <div class="mr-3">
                <img :src="ad.imageUrl" style="width: 130px; height: auto;" class="d-block rounded overflow-hidden" />
            </div>

            <!-- details -->
            <div class="flex-grow-1">
                <!-- title -->
                <h5 class="flex-grow-1 mb-1">
                    <b-badge v-if="isMine" variant="warning" class="mr-2">mine</b-badge>
                    <b-badge :variant="statusBadgeVariant" class="mr-1">{{ad.status}}</b-badge>
                    {{ad.textbookTitle}} ({{ad.author}})
                </h5>

                <!-- description -->
                <div class="text-muted">
                    {{ad.description}}
                </div>

                <!-- buttons -->
                <div class="d-flex mt-2" v-if="isMine || ad.status==='available'">
                    <!-- request button -->
                    <button
                            :disabled="removing"
                            class="btn btn-light border mr-1 text-nowrap"
                            @click="request"
                            v-if="ad.status==='available' && !isMine"
                    >
                        <fa-icon icon="hand-holding-heart" class="mr-1" />
                        Request
                    </button>

                    <!-- edit button -->
                    <button
                            class="btn btn-outline-info border mr-2 text-nowrap"
                            @click="edit"
                            v-if="isMine"
                            :disabled="removing"
                    >
                        <fa-icon icon="edit" />
                        Edit
                    </button>

                    <!-- delete button -->
                    <button
                            class="btn btn-outline-danger border text-nowrap"
                            @click="remove"
                            v-if="isMine"
                            :disabled="removing"
                    >
                        <fa-icon v-if="removing" icon="circle-notch" spin fixed-width />
                        <fa-icon v-else icon="trash" fixed-width />
                        Remove
                    </button>
                </div>

                <!-- show reviews button -->
                <button
                        v-if="!showReviews"
                        class="btn btn-link m-0 mt-2 p-0 text-nowrap"
                        @click="clickReviewButton"
                        :disabled="loadingReviews"
                >
                    <fa-icon v-if="loadingReviews" icon="circle-notch" spin fixed-width class="mr-1" />
                    <fa-icon v-else icon="chevron-down" fixed-width class="mr-1" />
                    {{loadingReviews ? 'Loading reviews' : 'Show Reviews'}}
                </button>

            </div>
        </div>

        <!-- reviews -->
        <div style="margin-left: 130px" class="mt-3">

            <div v-if="showReviews" style="margin-left: -1.25em">

                <!-- no reviews, not signed in message -->
                <div v-if="reviews.length === 0 && !signedIn" class="d-flex mb-3 text-muted">
                    <fa-icon icon="kiwi-bird" class="mr-3 mt-1" fixed-width />
                    <small class="d-block">
                        There are no reviews posted for this book yet. Sign in to post the first review.
                    </small>
                </div>

                <!-- post review form -->
                <div class="d-flex mb-3 align-items-center" v-if="signedIn">
                    <fa-icon icon="quote-left" class="mr-3 mt-1" fixed-width />
                    <b-form-input
                            :placeholder="reviews.length === 0 ? 'Post the first review...' : 'Enter your review...'"
                            v-model="reviewText"
                            class="mr-2"
                            :readonly="postingReview || loadingReviews"
                            @keypress.enter="postReview"
                    />
                    <button
                            class="btn btn-light border text-nowrap"
                            :disabled="!reviewText || loadingReviews || postingReview"
                            @click="postReview"
                    >
                        Post
                        <fa-icon v-if="postingReview" icon="circle-notch" spin fixed-width class="ml-1" />
                        <fa-icon v-else icon="paper-plane" fixed-width class="ml-1" />
                    </button>
                </div>

                <!-- list of reviews -->
                <div v-for="review in reviews" :key="review.id" class="d-flex mb-3">
                    <fa-icon icon="quote-left" class="mr-3 mt-1" fixed-width />
                    <div class="flex-grow-1">
                        <div>
                            <b-badge class="mr-1" v-if="review.userId === currentUserId" variant="warning">mine</b-badge>
                            {{review.reviewText}}
                        </div>
                        <small class="text-muted d-flex mt-1">
                            <div class="flex-grow-1">
                                {{review.dateAdded.format('h:mm A, MMMM D, YYYY')}}
                            </div>
                            <div class="text-muted" v-if="review.userId === currentUserId && review._removing">
                                Remove review
                                <fa-icon icon="circle-notch" spin fixed-width class="mr-1" />
                            </div>
                            <a href="#" v-else-if="review.userId === currentUserId" @click="removeReview(review)">
                                Remove review
                                <fa-icon icon="trash" fixed-width class="mr-1" />
                            </a>
                        </small>
                    </div>
                </div>
            </div>

            <!-- hide reviews button -->
            <button
                    v-if="showReviews"
                    class="btn btn-link text-nowrap mt-0 pt-0"
                    @click="clickReviewButton"
                    :disabled="removing || loadingReviews"
            >
                <fa-icon v-if="loadingReviews" icon="circle-notch" spin fixed-width class="mr-1" />
                <fa-icon v-else icon="chevron-up" fixed-width class="mr-1" />
                {{loadingReviews ? 'Loading reviews' : 'Hide Reviews'}}
            </button>
        </div>
    </div>
</template>

<script>
    import moment from 'moment';

    export default {
        props: ['ad', 'currentUserId', 'signedIn'],
        data: () => ({
            showReviews: false,
            removing: false,
            loadingReviews: false,
            postingReview: false,
            reviews: [],
            reviewText: null,
        }),
        computed: {
            statusBadgeVariant() {
                if (this.ad.status === 'available') {
                    return 'success';
                } else if (this.ad.status === 'unavailable') {
                    return 'danger';
                }
                return 'secondary';
            },
            isMine() {
                return this.ad.userId === this.currentUserId;
            },
        },
        methods: {
            async removeReview(review) {
                review._removing = true;
                try {
                    await this.$sharebook.delete(`/review/${review.id}`);
                } catch (error) {
                    alert(`Something went wrong removing this review: ${error}`);
                }
                this.loadReviews();
            },
            async postReview() {
                if (!this.postingReview) {
                    this.postingReview = true;
                    try {
                        const params = new URLSearchParams();
                        params.append('reviewText', this.reviewText);
                        await this.$sharebook.post(`/review?adId=${this.ad.id}`, params);
                    } catch (error) {
                        alert(`There was a problem posting your review: ${error}`);
                    }
                    this.postingReview = false;
                    this.loadReviews();
                }
            },
            clickReviewButton() {
                if (this.showReviews) {
                    this.showReviews = false;
                } else {
                    this.loadReviews();
                }
            },
            async loadReviews() {
                this.loadingReviews = true;
                try {
                    const dateFormat = 'MMMM DD, YYYY [at] h:mm:ss A';
                    const { data: reviewsMap } = await this.$sharebook.get(`/review?adId=${this.ad.id}`);
                    this.reviews = Object.entries(reviewsMap)
                        .map(entry => ({
                            ...entry[1],
                            dateAdded: moment(entry[1].dateAdded, dateFormat),
                            dateModified: moment(entry[1].dateModified, dateFormat),
                            id: entry[0],
                            _removing: false,
                        }))
                        .sort((a, b) => b.dateModified.unix() - a.dateModified.unix());
                    this.reviewText = null;
                    this.showReviews = true;
                } catch (error) {
                    alert(`There was a problem loading the reviews for this book: ${error}`);
                }
                this.loadingReviews = false;
            },
            async edit() {
                alert('Not implemented');
            },
            async request() {
                alert('Not implemented');
            },
            async remove() {
                if (confirm(`Are you sure you want to delete the list for ${this.ad.textbookTitle}?`)) {
                    this.removing = true;
                    try {
                        await this.$sharebook.delete(`/ad/${this.ad.id}`);
                    } catch (error) {
                        this.removing = false;
                        alert(error);
                    }
                    this.$emit('change');
                }
            },
        },
    }
</script>
