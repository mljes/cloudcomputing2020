import Vue from 'vue';
import App from './App.vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import axios from 'axios';
import auth from './auth';

library.add(fas, fab, far);
Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.component('fa-icon', FontAwesomeIcon);

// setup axios
// const sharebook = axios.create({ baseURL: 'http://3.95.153.203:5000' }); // production
const sharebook = axios.create({ baseURL: 'http://localhost:5000' }); // local
Vue.prototype.$sharebook = sharebook;
let tokenRenewalTimeout = null;

async function renewToken() {
    if (!auth.signedIn()) {
        return;
    }
    try {
        const { data: tokens } = await sharebook.get('/refreshtoken', {
            headers: {
                Authorization: `Bearer ${auth.getRefreshToken()}`,
            },
        });
        auth.setTokens(tokens);
    } catch (error) {
        auth.clearTokens();
        console.error(error);
    }
}

sharebook.interceptors.request.use(config => {
    if (auth.signedIn()) {
        config.headers['Authorization'] = config.headers['Authorization'] || `Bearer ${auth.getIdToken()}`;
    }
    return config;
});

if (auth.signedIn()) {
    renewToken();
}

auth.onChange(() => {
    if (auth.signedIn()) {
        if (tokenRenewalTimeout) {
            clearTimeout(tokenRenewalTimeout);
        }
        tokenRenewalTimeout = setTimeout(renewToken, auth.getIdTokenExpiry() - Date.now());
    }
});

new Vue({
    render: h => h(App),
}).$mount('#app');
