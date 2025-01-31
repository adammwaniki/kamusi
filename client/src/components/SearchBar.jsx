import { useState, useEffect } from 'react';
import { TextField, Autocomplete, CircularProgress } from '@mui/material';
import useDebounce from '../hooks/useDebounce';
import useSearch from '../hooks/useSearch';

export default function SearchBar() {
  const [query, setQuery] = useState('');
  const debouncedQuery = useDebounce(query, 300);
  const { results, isLoading, error } = useSearch(debouncedQuery);

  return (
    <div>
      <Autocomplete
        freeSolo
        options={results}
        loading={isLoading}
        onInputChange={(e, newValue) => setQuery(newValue)}
        renderInput={(params) => (
          <TextField
            {...params}
            label="Search Swahili Words"
            variant="outlined"
            fullWidth
            InputProps={{
              ...params.InputProps,
              endAdornment: (
                <>
                  {isLoading ? <CircularProgress size={20} /> : null}
                  {params.InputProps.endAdornment}
                </>
              )
            }}
          />
        )}
        getOptionLabel={(option) => option.word}
        renderOption={(props, option) => (
          <li {...props} key={option.id}>
            <div>
              <strong>{option.word}</strong>
              <div>{option.translation}</div>
            </div>
          </li>
        )}
      />
    </div>
  );
}