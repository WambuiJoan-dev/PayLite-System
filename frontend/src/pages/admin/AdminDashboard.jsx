import React, { useState, useEffect } from 'react';
import { Box, Typography, Grid, Paper, CircularProgress } from '@mui/material';
import api from '../../services/api';

const AdminDashboard = () => {
  const [stats, setStats] = useState({ customers: 0, phones: 0, sales: 0, payments: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const [custRes, phoneRes, saleRes, payRes] = await Promise.all([
          api.get('/customers').catch(() => ({ data: [] })),
          api.get('/phones').catch(() => ({ data: [] })),
          api.get('/sales').catch(() => ({ data: [] })),
          api.get('/payments').catch(() => ({ data: [] })),
        ]);
        setStats({
          customers: custRes.data.length || 0,
          phones: phoneRes.data.length || 0,
          sales: saleRes.data.length || 0,
          payments: payRes.data.length || 0,
        });
      } catch (error) {
        console.error("Error fetching stats:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  if (loading) return <Box display="flex" justifyContent="center" mt={4}><CircularProgress /></Box>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Admin Dashboard</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={3}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Typography variant="h6">Total Customers</Typography>
            <Typography variant="h3">{stats.customers}</Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Typography variant="h6">Total Phones</Typography>
            <Typography variant="h3">{stats.phones}</Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Typography variant="h6">Total Sales</Typography>
            <Typography variant="h3">{stats.sales}</Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Typography variant="h6">Total Payments</Typography>
            <Typography variant="h3">{stats.payments}</Typography>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default AdminDashboard;
