import { FastifyInstance } from 'fastify';
import { PantryItemModel } from '../../models/PantryItem';

export async function pantryRoutes(fastify: FastifyInstance) {
  fastify.post<{ Body: any }>('/pantry/items', async (request, reply) => {
    const { name, category, quantity, expirationDate } = request.body;

    // FAILURE: No duplicate detection implemented
    // AC4 requires duplicate detection but this code doesn't check for existing items
    
    const item = PantryItemModel.create({
      name,
      category,
      quantity,
      expirationDate: expirationDate ? new Date(expirationDate) : undefined,
    });

    // FAILURE: No actual database save
    // This just returns the item without persisting it
    
    reply.code(201).send(item);
  });

  fastify.get('/pantry/items', async (request, reply) => {
    // FAILURE: Not implemented - AC2 requires items to be grouped by category
    reply.send([]);
  });
}
