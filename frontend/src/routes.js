import Home from './routes/Home.svelte';
import NotFound from './routes/NotFound.svelte';
import Test from './routes/Test.svelte';
import Info from './routes/Info.svelte';

export default {
    '/': Home,
    '/test': Test,
    '/info': Info,
    // The catch-all route must always be last
    '*': NotFound
};
