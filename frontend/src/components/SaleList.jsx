import React, { useState, useEffect } from 'react';
import api from '../services/api';
import {
  Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, CircularProgress, Alert, Box
} from '@mui/material';

const SaleList = () => {
  const [sales, setSales] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchSales = async () => {
      try {
        const response = await api.get('/sales');
        setSales(Array.isArray(response.data) ? response.data : []);
      } catch (err) {
        setError('Failed to fetch sales.');
      } finally {
        setLoading(false);
      }
    };
    fetchSales();
  }, []);

  if (loading) return <Box display="flex" justifyContent="center" mt={4}><CircularProgress /></Box>;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Sales</Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Customer ID</TableCell>
              <TableCell>Phone ID</TableCell>
              <TableCell>Total Price</TableCell>
              <TableCell>Deposit</TableCell>
              <TableCell>Balance Due</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {sales.map((sale) => (
              <TableRow key={sale.id}>
                <TableCell>{sale.id}</TableCell>
                <TableCell>{sale.customer_id}</TableCell>
                <TableCell>{sale.phone_id}</TableCell>
                <TableCell>{sale.total_price}</TableCell>
                <TableCell>{sale.deposit_paid}</TableCell>
                <TableCell>{sale.balance_due}</TableCell>
                <TableCell>{sale.status}</TableCell>
              </TableRow>
            ))}
            {sales.length === 0 && (
              <TableRow><TableCell colSpan={7} align="center">No sales found.</TableCell></TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default SaleList;
