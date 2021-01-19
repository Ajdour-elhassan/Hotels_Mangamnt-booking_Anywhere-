const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();



// vue app
const app = Vue.createApp({
    data() {
        return {
            item: 'first_name',
            num: 1,
        };
    },
    methods: {
        formItem() {
            return this.item;
        },
    }
});
app.amount('#userform');