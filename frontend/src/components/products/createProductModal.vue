<script setup lang="js">
import { VueFinalModal } from 'vue-final-modal'
import Button from '../ui/button/Button.vue'

const product = {
    name: '',
    description: '',
    image: ''
}

const emit = defineEmits()

const cleanProduct = () => {
    product.name = ''
    product.description = ''
    product.image = ''
}

const handleCreateProduct = async () => {
    try {
        const formData = new FormData()
        formData.append('name', product.name)
        formData.append('description', product.description)
        formData.append('image', product.image)
    
        const response = await fetch(`${import.meta.env.VITE_API_URL}/products`, {
            method: 'POST',
            body: formData
        })

        if (response.status !== 201) {
            throw new Error('Não foi possível criar o produto!')
        }
    
        cleanProduct()
        await emit('confirm')
    } catch (error) {
        alert('Não foi possível criar o produto!')
    }
}
</script>

<template>
    <VueFinalModal class="confirm-modal" content-class="confirm-modal-content" overlay-transition="vfm-fade"
        content-transition="vfm-fade">
        <h2 class="text-2xl font-bold text-gray-600">Criar novo produto</h2>
        <hr>

        <div class="flex flex-col gap-4">
            <div class="flex flex-col gap-2">
                <label for="name">Nome do Produto:</label>
                <input class="border border-gray-400 rounded-md p-2" name="name" v-model="product.name" />
            </div>

            <div class="flex flex-col gap-2">
                <label for="description">Descrição:</label>
                <textarea class="border border-gray-400 rounded-md p-2" name="description"
                    v-model="product.description" />
            </div>

            <div class="flex flex-col gap-2">
                <label for="image">Imagem do produto:</label>
                <input class="border border-gray-400 rounded-md p-2" type="file" name="image"
                    @change="product.image = $event.target.files[0]" />
            </div>
        </div>

        <Button @click="handleCreateProduct" variant="secondary">
            Salvar
        </Button>
    </VueFinalModal>
</template>

<style>
.confirm-modal {
    display: flex;
    justify-content: center;
    align-items: center;
}

.confirm-modal-content {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    background: #fff;
    border-radius: 0.5rem;
}

.confirm-modal-content>*+* {
    margin: 0.5rem 0;
}

.confirm-modal-content h1 {
    font-size: 1.375rem;
}

.confirm-modal-content button {
    margin: 0.25rem 0 0 auto;
    padding: 0 8px;
    border: 1px solid;
    border-radius: 0.5rem;
}

.dark .confirm-modal-content {
    background: #000;
}
</style>