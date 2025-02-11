import izitoast from 'izitoast';
import 'izitoast/dist/css/iziToast.min.css';

izitoast.settings({
    timeout: 3000,
    displayMode: 2,
    position: 'topRight',
});

const plugin = {
    install(app, options) {
        let props = {};
        let types = ['info', 'success', 'warning', 'error'];

        types.forEach(type => {
            props[type] = function (message, settings = {}) {
                izitoast[type]({ message, ...settings });
            }
        });

        app.config.globalProperties.$toast = props;
    }
};

export default plugin;
