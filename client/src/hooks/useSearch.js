import { useState, useEffect } from 'react';
import api from '../services/api';

export default function useSearch(query) {
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!query) {
      setResults([]);
      return;
    }

    const search = async () => {
      setIsLoading(true);
      try {
        const response = await api.get(`/search?q=${encodeURIComponent(query)}`);
        setResults(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setIsLoading(false);
      }
    };

    search();
  }, [query]);

  return { results, isLoading, error };
}