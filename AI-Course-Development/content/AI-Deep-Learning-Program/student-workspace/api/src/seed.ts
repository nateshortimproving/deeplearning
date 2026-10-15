import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

async function main() {
  // Clear existing data
  await prisma.pantryItem.deleteMany({});

  // Seed test data
  const items = await prisma.pantryItem.createMany({
    data: [
      {
        name: "Milk",
        quantity: 1,
        unit: "gallon",
        category: "Dairy",
        expirationDate: new Date("2026-10-20"),
      },
      {
        name: "Eggs",
        quantity: 12,
        unit: "count",
        category: "Dairy",
        expirationDate: new Date("2026-10-25"),
      },
      {
        name: "Apples",
        quantity: 4,
        unit: "count",
        category: "Produce",
        expirationDate: new Date("2026-10-18"),
      },
      {
        name: "Carrots",
        quantity: 2,
        unit: "lbs",
        category: "Produce",
        expirationDate: new Date("2026-10-30"),
      },
      {
        name: "Bread",
        quantity: 1,
        unit: "loaf",
        category: "Grains",
        expirationDate: new Date("2026-10-17"),
      },
      {
        name: "Rice",
        quantity: 5,
        unit: "lbs",
        category: "Grains",
        expirationDate: new Date("2027-10-14"),
      },
    ],
  });

  console.log(`Seeded ${items.count} pantry items`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
