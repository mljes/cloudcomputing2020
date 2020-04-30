import jwtDecode from 'jwt-decode';

let changeCallbacks = [];

const auth = {
    setTokens(tokens) {
        localStorage.setItem('REFRESH_TOKEN', tokens.refreshToken);
        localStorage.setItem('ID_TOKEN', tokens.idToken);
        changeCallbacks.forEach(cb => cb.callback());
    },
    clearTokens() {
        localStorage.removeItem('REFRESH_TOKEN');
        localStorage.removeItem('ID_TOKEN');
        changeCallbacks.forEach(cb => cb.callback());
    },
    onChange(callback) {
        const id = Symbol();
        changeCallbacks.push({ callback, id });
        callback();
        return id;
    },
    unsubscribe(id) {
        changeCallbacks = changeCallbacks.filter(cb => cb.id === id);
    },
    getIdToken() {
        return localStorage.getItem('ID_TOKEN');
    },
    getRefreshToken() {
        return localStorage.getItem('REFRESH_TOKEN');
    },
    getEmail() {
        const token = localStorage.getItem('ID_TOKEN');
        if (token) {
            return jwtDecode(token).email;
        }
        return null;
    },
    getUserId() {
        const token = localStorage.getItem('ID_TOKEN');
        if (token) {
            return jwtDecode(token).user_id;
        }
        return null;
    },
    getIdTokenExpiry() {
        const token = localStorage.getItem('ID_TOKEN');
        if (token) {
            return 1000*jwtDecode(token).exp;
        }
        return null;
    },
    signedIn() {
        const refreshToken = localStorage.getItem('REFRESH_TOKEN');
        const idToken = localStorage.getItem('ID_TOKEN');
        return refreshToken && idToken;
    }
};

export default auth;
