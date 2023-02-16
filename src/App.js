import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Provider } from 'react-redux';

import Error404 from './containers/errors/Error404';
import Home from './containers/pages/Home';
import store from './store';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="*" element={<Error404 />} />
          <Route path="/" element={<Home />} />
          <Route path="/casos" element={<Cases />} />
          <Route path="/services" element={<Home />} />
          <Route path="/nosotros" element={<Home />} />
          <Route path="/carreras" element={<Home />} />
          <Route path="/blog" element={<Home />} />
          <Route path="/contacto" element={<Home />} />
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
