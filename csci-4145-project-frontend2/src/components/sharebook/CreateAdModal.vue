<template>
    <b-modal v-model="modalOpen" title="Add Listing">
        <b-form-group label="Title" label-for="input-1">
            <b-form-input
                    id="input-1"
                    v-model="ad.textbookTitle"
                    required
                    placeholder="Enter the textbook title"
                    :readonly="loading"
                    :state="showValidation && !ad.textbookTitle ? false : null"
            ></b-form-input>
        </b-form-group>

        <b-form-group label="Author" label-for="input-2">
            <b-form-input
                    id="input-2"
                    v-model="ad.author"
                    required
                    placeholder="Enter the textbook author"
                    :readonly="loading"
                    :state="showValidation && !ad.author ? false : null"
            ></b-form-input>
        </b-form-group>

        <b-form-group label="Description" label-for="input-3">
            <b-form-textarea
                    id="input-3"
                    v-model="ad.description"
                    required
                    placeholder="Enter the textbook description"
                    :readonly="loading"
                    :state="showValidation && !ad.description ? false : null"
            ></b-form-textarea>
        </b-form-group>

        <b-form-group label="Cover Image" label-for="input-4">
            <b-form-file
                    id="input-4"
                    v-model="ad.image"
                    placeholder="Select an image of the book's cover"
                    :readonly="loading"
            ></b-form-file>
        </b-form-group>

        <div v-if="error" class="bg-danger text-white rounded p-2">
            <fa-icon icon="exclamation-triangle" class="mr-1" />
            Something went wrong posting your ad: {{error}}
        </div>

        <template v-slot:modal-footer>
            <button class="btn btn-secondary" @click="modalOpen=false" :disabled="loading">
                <fa-icon icon="times" fixed-width />
                Cancel
            </button>
            <button class="btn btn-primary" @click="post" :disabled="loading">
                <fa-icon v-if="loading" icon="circle-notch" spin fixed-width />
                <fa-icon v-else icon="plus" fixed-width />
                Add Listing
            </button>
        </template>
    </b-modal>
</template>

<script>
    export default {
        props: ['value'],
        data: () => ({
            ad: {
                textbookTitle: null,
                description: null,
                author: null,
                image: null,
            },
            loading: false,
            error: 'Something went wrong',
            showValidation: false,
            modalOpen: false,
        }),
        methods: {
            validate() {
                this.showValidation = true;
                return this.ad.textbookTitle && this.ad.description && this.ad.author;
            },
            async post() {
                if (this.validate()) {
                    this.loading = true;
                    try {
                        const formData = new FormData();
                        formData.append('textbookTitle', this.ad.textbookTitle);
                        formData.append('description', this.ad.description);
                        formData.append('author', this.ad.author);
                        formData.append('image', this.ad.image);
                        await this.$sharebook.post('/ad', formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data',
                            },
                        });
                        this.error = null;
                        this.$emit('input', false);
                        this.$emit('ad-created');
                    } catch (error) {
                        this.error = error;
                    }
                    this.loading = false;
                }
            }
        },
        watch: {
            value(v) {
                this.modalOpen = v;
            },
            modalOpen(mo) {
                this.$emit('input', mo);
                if (mo) {
                    this.ad = {
                        textbookTitle: null,
                        description: null,
                        author: null,
                    };
                    this.loading = false;
                    this.error = null;
                    this.showValidation = false;
                }
            }
        }
    }
</script>
