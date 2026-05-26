import React, { useState, useEffect } from 'react';
import { Box, Typography, Paper, CircularProgress } from '@mui/material';
import api from '../../services/api';
import { getUserInfo } from '../../utils/auth';

const UserDashboard = () => {
  const [userInfo, setUserInfo] = useState(null);
  
  useEffect(() => {
    setUserInfo(getUserInfo());
  }, []);

  if (!userInfo) return <Box display="flex" justifyContent="center" mt={4}><CircularProgress /></Box>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>User Dashboard</Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="h6">Welcome, User {userInfo.id}!</Typography>
        <Typography variant="body1" sx={{ mt: 1 }}>
          Your role is: <strong>{userInfo.role}</strong>
        </Typography>
        <Typography variant="body2" color="textSecondary" sx={{ mt: 2 }}>
          From here you can view Customers, Phones, Sales, and Payments assigned to your operations.
        </Typography>
      </Paper>
    </Box>
  );
};

export default UserDashboard;
