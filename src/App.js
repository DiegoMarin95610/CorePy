import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import store from './store'
import { Provider } from 'react-redux';
import Error404 from './containers/errors/Error404';
import Home from './containers/pages/home';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route>
            {/* Error Display */}
            <Route path='*' element={<Error404 />} />
          
            {/* Home Display */}
            <Route path='/' element={<Home />} />
          </Route>
        </Routes>
      </Router>
    </Provider>
    
  );
}

export default App;
