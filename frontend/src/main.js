import { createApp } from 'vue'
import { createVfm } from 'vue-final-modal'
import App from './App.vue'

import './assets/index.css'
import 'vue-final-modal/style.css'

const app = createApp(App)

const vfm = createVfm()
app.use(vfm).mount('#app')
