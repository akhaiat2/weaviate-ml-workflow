// pages/api/search.js

const weaviate = require('weaviate-client');

export default async function handler(req, res) {
  const { query } = req.body;

  const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8080'
  });

  try {
    const result = await client.graphql
      .get()
      .withClassName('Article')
      .withFields(['text'])
      .withWhere({
        operator: 'Equal',
        path: ['text'],
        valueText: query
      })
      .do();

    res.status(200).json({ results: result.data.Get.Article });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
