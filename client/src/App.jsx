import { ThemeProvider, CssBaseline, Container } from '@mui/material';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import theme from './styles/theme';
import SearchBar from './components/SearchBar';
import WordDetail from './components/WordDetail';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<SearchBar />} />
            <Route path="/word/:wordId" element={<WordDetail />} />
          </Routes>
        </BrowserRouter>
      </Container>
    </ThemeProvider>
  );
}

export default App