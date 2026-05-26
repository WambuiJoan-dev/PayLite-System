import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import theme from './theme';
import LoginPage from './LoginPage';
import Layout from './Layout';
import CustomerList from './components/CustomerList';
import PhoneList from './components/PhoneList';
import SaleList from './components/SaleList';
import PaymentList from './components/PaymentList';
import AdminDashboard from './pages/admin/AdminDashboard';
import UserDashboard from './pages/user/UserDashboard';
import RoleRoute from './components/RoleRoute';
import { getUserRole, isAuthenticated } from './utils/auth';

const IndexRedirect = () => {
  if (!isAuthenticated()) return <Navigate to="/login" replace />;
  const role = getUserRole();
  return <Navigate to={role === 'admin' ? '/admin' : '/user'} replace />;
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          
          <Route path="/" element={<IndexRedirect />} />

          {/* Admin Routes */}
          <Route path="/admin" element={<RoleRoute allowedRoles={['admin']}><Layout /></RoleRoute>}>
            <Route index element={<AdminDashboard />} />
            <Route path="customers" element={<CustomerList />} />
            <Route path="phones" element={<PhoneList />} />
            <Route path="sales" element={<SaleList />} />
            <Route path="payments" element={<PaymentList />} />
          </Route>

          {/* User Routes */}
          <Route path="/user" element={<RoleRoute allowedRoles={['user', 'admin']}><Layout /></RoleRoute>}>
            <Route index element={<UserDashboard />} />
            <Route path="customers" element={<CustomerList />} />
            <Route path="phones" element={<PhoneList />} />
            <Route path="sales" element={<SaleList />} />
            <Route path="payments" element={<PaymentList />} />
          </Route>

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
