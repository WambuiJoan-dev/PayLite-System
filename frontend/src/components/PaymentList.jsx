import React, { useState, useEffect } from 'react';
import api from '../services/api';
import {
  Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, CircularProgress, Alert, Box
} from '@mui/material';

const PaymentList = () => {
  const [payments, setPayments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPayments = async () => {
      try {
        const response = await api.get('/payments');
        setPayments(Array.isArray(response.data) ? response.data : []);
      } catch (err) {
        setError('Failed to fetch payments.');
      } finally {
        setLoading(false);
      }
    };
    fetchPayments();
  }, []);

  if (loading) return <Box display="flex" justifyContent="center" mt={4}><CircularProgress /></Box>;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Payments</Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Sale ID</TableCell>
              <TableCell>Amount Paid</TableCell>
              <TableCell>Date Paid</TableCell>
              <TableCell>Next Due Date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {payments.map((payment) => (
              <TableRow key={payment.id}>
                <TableCell>{payment.id}</TableCell>
                <TableCell>{payment.sale_id}</TableCell>
                <TableCell>{payment.amount_paid}</TableCell>
                <TableCell>{new Date(payment.date_paid).toLocaleDateString()}</TableCell>
                <TableCell>{payment.next_due_date ? new Date(payment.next_due_date).toLocaleDateString() : 'N/A'}</TableCell>
              </TableRow>
            ))}
            {payments.length === 0 && (
              <TableRow><TableCell colSpan={5} align="center">No payments found.</TableCell></TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default PaymentList;
