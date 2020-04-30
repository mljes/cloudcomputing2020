

<template>
    <div class="d-flex flex-column position-fixed" style="top:0; bottom:0; left:0; right:0">
        <Menu @change-page="p => page = p" />
        <div class="flex-grow-1 overflow-auto p-3">
            <component :is="$options.pages[page]" @change-page="p => page = p" />
        </div>
    </div>
</template>

<script>
    import Menu from "./components/Menu";
    import HomePage from "./components/HomePage"
    import HappyHoursPage from "./components/HappyHoursPage";
    import DiscountsPage from "./components/DiscountsPage";
    import SharebookPage from "./components/SharebookPage";

    export default {
        name: 'App',
        components: {
            Menu,
            HomePage,
            HappyHoursPage,
            DiscountsPage,
            SharebookPage,
        },
        pages: {
            home: HomePage,
            happyHours: HappyHoursPage,
            discounts: DiscountsPage,
            sharebook: SharebookPage,
        },
        data: () => ({
            page: 'home',
        }),
    }
</script>
