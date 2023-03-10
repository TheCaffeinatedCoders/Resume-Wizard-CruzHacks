import Home from './routes/Home.svelte';
import NotFound from './routes/NotFound.svelte';
import Test from './routes/Test.svelte';
import Info from './routes/Info.svelte';
import Cat from './routes/Cat.svelte';
import Completion from './routes/Completion.svelte';

export default {
    '/': Home,
    '/test': Test,
    '/info': Info,
    '/cat': Cat,
    '/completion': Completion,
    // The catch-all route must always be last
    '*': NotFound
};
