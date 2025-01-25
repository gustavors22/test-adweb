<script setup>
import Button from '@/components/ui/button/Button.vue'

const props = defineProps({
    products: { type: Array, required: true },
    handleDeleteProduct: { type: Function, required: true }
});
</script>

<template>
    <table class="min-w-full divide-y divide-gray-200 rounded-lg">
        <thead class="bg-gray-50">
            <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Nome
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Imagem
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Descrição
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Ações
                </th>
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="product in products" :key="product.name">
                <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-sm text-gray-900">{{ product.name }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                    <img class="h-20 w-20 rounded-lg" :src="product.image" alt="" srcset="">
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                        <p class="truncate max-w-[200px] overflow-hidden whitespace-nowrap text-sm text-gray-900 center">{{ product.description }}</p>
                </td>
                <td class="px-2 py-4">
                    <Button variant="destructive" @click="handleDeleteProduct(product.id)">Excluir</Button>
                </td>
            </tr>
        </tbody>
    </table>
</template>
