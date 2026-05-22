import Fastify from 'fastify'

const fastify = Fastify({
    logger: true
});

// Create a routes for homepage and about
fastify.get('/', async function handler (request, reply) {
    return { message: 'Hello, World!' };
});

fastify.get('/about', async function handler (request, reply) {
    return { info: 'About information' };
});

// Run web server
try {
    await fastify.listen({ 
        host: "0.0.0.0", 
        port: 4000
    });
} catch (err) {
    fastify.log.error(err);
    process.exit(1);
}