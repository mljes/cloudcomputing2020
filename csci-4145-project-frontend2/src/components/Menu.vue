<template>
    <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand href="#" @click="$emit('change-page', 'home')">
            Life as a Student
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item href="#" @click="$emit('change-page', 'home')">Home</b-nav-item>
                <b-nav-item href="#" @click="$emit('change-page', 'sharebook')">Sharebook</b-nav-item>
                <b-nav-item href="#" @click="$emit('change-page', 'happyHours')">Happy Hours</b-nav-item>
                <b-nav-item href="#" @click="$emit('change-page', 'discounts')">Discounts</b-nav-item>
            </b-navbar-nav>

            <div class="ml-auto" />
            <fa-icon spin icon="circle-notch" size="lg" class="text-muted" v-if="loading" />
            <b-navbar-nav>
                <b-nav-item-dropdown :text="loading ? '' : email" right v-if="signedIn">
                    <b-dropdown-item href="#" @click="signOut">Sign Out</b-dropdown-item>
                </b-nav-item-dropdown>
                <b-nav-item-dropdown :text="loading ? '' : 'Sign in'" right v-else>
                    <b-dropdown-form>
                        <b-form-group label="Email" label-for="dropdown-form-email" @submit.stop.prevent>
                            <b-form-input
                                    v-model="email"
                                    id="dropdown-form-email"
                                    size="sm"
                                    placeholder="email@example.com"
                                    :readonly="loading"
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group label="Password" label-for="dropdown-form-password">
                            <b-form-input
                                    v-model="password"
                                    id="dropdown-form-password"
                                    type="password"
                                    size="sm"
                                    placeholder="Password"
                                    :readonly="loading"
                            ></b-form-input>
                        </b-form-group>
                        <div class="d-flex text-nowrap py-2">
                            <b-button variant="secondary" size="sm" @click="createAccount" :disabled="loading">
                                <fa-icon icon="user-circle" />
                                Create Account
                            </b-button>
                            <div class="flex-grow-1 mx-2"></div>
                            <b-button variant="primary" size="sm" @click="signIn" :disabled="loading">
                                Sign In
                                <fa-icon icon="sign-in-alt" />
                            </b-button>
                        </div>
                    </b-dropdown-form>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
    import auth from "../auth";

    export default {
        data: () => ({
            email: null,
            password: null,
            signedIn: false,
            loading: false,
        }),
        created() {
            auth.onChange(() => {
                this.password = null;
                if (auth.signedIn()) {
                    this.signedIn = true;
                    this.email = auth.getEmail();
                } else {
                    this.signedIn = false;
                }
            });
        },
        methods: {
            async signIn() {
                this.loading = true;
                try {
                    const { data: tokens } = await this.$sharebook.get('/login', {
                        auth: {
                            username: this.email,
                            password: this.password,
                        },
                    });
                    auth.setTokens({
                        idToken: tokens.id_token,
                        refreshToken: tokens.refresh_token,
                    });
                } catch (error) {
                    alert(error);
                }
                this.loading = false;
            },
            async signOut() {
                auth.clearTokens();
            },
            async createAccount() {
                this.loading = true;
                try {
                    await this.$sharebook.post('/createaccount', {
                        email: this.email,
                        password: this.password,
                    });
                    const { data: tokens } = await this.$sharebook.get('/login', {
                        auth: {
                            username: this.email,
                            password: this.password,
                        },
                    });
                    auth.setTokens(tokens);
                    alert(`Welcome to Life as a Student, ${this.email}!`);
                } catch (error) {
                    alert(error);
                }
                this.loading = false;
            },
        }
    }
</script>

