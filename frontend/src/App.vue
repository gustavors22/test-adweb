<script setup>
import { ModalsContainer, useModal } from 'vue-final-modal'

import ProductsTable from './components/products/productsTable.vue';
import Button from './components/ui/button/Button.vue'
import CreateProductModal from './components/products/createProductModal.vue';

import { onMounted, ref } from 'vue';

const products = ref([])

const handleGetProducts = async () => {
  const response = await fetch(`${import.meta.env.VITE_API_URL}/products`)
  products.value = await response.json()
}

const handleDeleteProduct = async (id) => {
  await fetch(`${import.meta.env.VITE_API_URL}/products/${id}`, {
    method: 'DELETE'
  })

  await handleGetProducts()
}

onMounted(async () => {
  await handleGetProducts()
})

const { open, close } = useModal({
    component: CreateProductModal,
    attrs: {
      onConfirm() {
        handleGetProducts()
        close()
      },
    },
    slots: {
      default: '<p>The content of the modal</p>',
    },
  })

</script>

<template>
  <div class="p-8">
    <h2 class="text-2xl font-bold mb-4 text-gray-600">Produtos</h2>
    <div class="mt-16 flex flex-col gap-8">
      <div class="flex justify-end">
        <Button variant="secondary" @click="open">Novo produto</Button>
      </div>
      <ProductsTable :products="products" class="w-full" :handleDeleteProduct="handleDeleteProduct" />
    </div>
    <ModalsContainer />
  </div>
</template>

<style>
  .middle-center {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>