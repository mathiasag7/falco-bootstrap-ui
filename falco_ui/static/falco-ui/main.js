document.addEventListener('alpine:init', () => {
    Alpine.data('tabs', () => ({
        tabs: [],
        currentTab: null,
        isCurrent(tab) {
            return this.currentTab === tab
        },
        register(name) {
            this.tabs.push(name)
        }
    }))
})