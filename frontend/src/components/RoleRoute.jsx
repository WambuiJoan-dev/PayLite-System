import React from 'react';
import { Navigate } from 'react-router-dom';
import { isAuthenticated, getUserRole } from '../utils/auth';

const RoleRoute = ({ children, allowedRoles }) => {
  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }
  
  const userRole = getUserRole();
  if (allowedRoles && !allowedRoles.includes(userRole)) {
    // If user is logged in but doesn't have right role, redirect to their dashboard
    if (userRole === 'admin') return <Navigate to="/admin" replace />;
    return <Navigate to="/user" replace />;
  }

  return children;
};

export default RoleRoute;
