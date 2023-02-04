import Home from './routes/Home.svelte';
import NotFound from './routes/NotFound.svelte';
import Test from './routes/Test.svelte'

export default {
    '/': Home,
    '/test': Test,
    // The catch-all route must always be last
    '*': NotFound
};
