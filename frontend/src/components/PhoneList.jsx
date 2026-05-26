import React, { useState, useEffect } from 'react';
import api from '../services/api';
import {
  Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, CircularProgress, Alert, Box
} from '@mui/material';

const PhoneList = () => {
  const [phones, setPhones] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPhones = async () => {
      try {
        const response = await api.get('/phones');
        setPhones(Array.isArray(response.data) ? response.data : []);
      } catch (err) {
        setError('Failed to fetch phones.');
      } finally {
        setLoading(false);
      }
    };
    fetchPhones();
  }, []);

  if (loading) return <Box display="flex" justifyContent="center" mt={4}><CircularProgress /></Box>;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Phones</Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Brand</TableCell>
              <TableCell>Model</TableCell>
              <TableCell>Price</TableCell>
              <TableCell>Stock Quantity</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {phones.map((phone) => (
              <TableRow key={phone.id}>
                <TableCell>{phone.id}</TableCell>
                <TableCell>{phone.brand}</TableCell>
                <TableCell>{phone.model}</TableCell>
                <TableCell>{phone.price}</TableCell>
                <TableCell>{phone.stock_quantity}</TableCell>
              </TableRow>
            ))}
            {phones.length === 0 && (
              <TableRow><TableCell colSpan={5} align="center">No phones found.</TableCell></TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default PhoneList;
