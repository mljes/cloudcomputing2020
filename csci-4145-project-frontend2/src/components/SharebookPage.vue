<template>
    <div>
        <h1>
            <fa-icon icon="book" class="mr-1" />
            Sharebook
        </h1>
        <h3 class="text-muted font-italic mb-3">Textbook sharing service</h3>

        <div class="pt-2 pb-3 d-flex align-items-center">
            <!-- search bar -->
            <b-form-input
                    v-model="search" placeholder="Search..."
                    class="flex-grow-1 shadow"
                    :readonly="loading"
            />

            <!-- clear search button -->
            <button
                    v-if="search"
                    class="btn shadow-none"
                    @click="search=null"
                    :disabled="loading"
                    style="margin-left: -37px"
            >
                <fa-icon icon="times" />
            </button>

            <!-- new post button -->
            <button
                    v-if="signedIn"
                    class="btn btn-success ml-2 text-nowrap shadow"
                    @click="createAdModalOpen=true"
                    :disabled="loading"
            >
                <fa-icon icon="plus" class="mr-1" />
                Add Listing
            </button>

            <!-- reload button -->
            <button class="btn btn-secondary ml-2 text-nowrap shadow" @click="reload" :disabled="loading">
                <fa-icon icon="sync" :spin="loading" class="mr-1" />
                Reload
            </button>
        </div>

        <!-- loading message -->
        <h2 v-if="loading && ads.length === 0" class="text-center text-muted p-5 m-5">
            <fa-icon spin icon="circle-notch" size="lg" />
        </h2>

        <!-- error message -->
        <div v-else-if="error" class="text-danger p-3">
            There was a problem loading ads: {{error}}
        </div>

        <!-- no ads message -->
        <div v-else-if="ads.length === 0" class="p-3">
            Sorry, there are no ads to show. Use the button above to create one!
        </div>

        <!-- no results message -->
        <div v-else-if="filteredAds.length === 0" class="p-3">
            Sorry, there are no ads matching <b>{{search}}</b>. Try another search!
        </div>

        <!-- list of ads -->
        <div class="row">
            <ad
                    v-for="ad in filteredAds"
                    :key="ad.id"
                    :ad="ad"
                    :current-user-id="currentUserId"
                    :signed-in="signedIn"
                    @change="reload"
                    class="col-sm-12 col-lg-6 col-xl-4 p-3"
            />
        </div>

        <create-ad-modal v-model="createAdModalOpen" @ad-created="reload"/>
    </div>
</template>

<script>
    import Ad from "./sharebook/Ad";
    import CreateAdModal from "./sharebook/CreateAdModal";
    import auth from "../auth";

    export default {
        components: {CreateAdModal, Ad},
        data: () => ({
            loading: true,
            error: null,
            ads: [],
            search: null,
            createAdModalOpen: false,
            currentUserId: null,
            authCallbackId: null,
            signedIn: false,
        }),
        async created() {
            this.authCallbackId = auth.onChange(() => {
                this.currentUserId = auth.getUserId();
                this.signedIn = auth.signedIn();
            });
            this.reload();
        },
        beforeDestroy() {
            auth.unsubscribe(this.authCallbackId);
        },
        computed: {
            filteredAds() {
                if (!this.search) {
                    return this.ads;
                }
                return this.ads.filter(ad =>
                    ad.textbookTitle.toLowerCase().includes(this.search.toLowerCase())
                    || ad.description.toLowerCase().includes(this.search.toLowerCase())
                    || ad.author.toLowerCase().includes(this.search.toLowerCase())
                );
            },
        },
        methods: {
            async reload() {
                this.loading = true;
                try {
                    const { data: ads } = await this.$sharebook.get('/ad');
                    this.ads = Object.entries(ads).map(entry => ({
                        ...entry[1],
                        id: entry[0],
                    }));
                    this.error = null;
                } catch (error) {
                    this.error = error;
                }
                this.loading = false;
            }
        }
    }
</script>
