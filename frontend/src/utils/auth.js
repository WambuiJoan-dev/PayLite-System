import { jwtDecode } from 'jwt-decode';

export const getToken = () => localStorage.getItem('access_token');

export const getUserInfo = () => {
  const token = getToken();
  if (!token) return null;
  try {
    const decoded = jwtDecode(token);
    // flask-jwt-extended puts identity in 'sub'
    return decoded.sub || null;
  } catch (error) {
    return null;
  }
};

export const getUserRole = () => {
  const userInfo = getUserInfo();
  return userInfo ? userInfo.role : null;
};

export const isAuthenticated = () => {
  const token = getToken();
  if (!token) return false;
  try {
    const decoded = jwtDecode(token);
    // Check if token is expired
    if (decoded.exp * 1000 < Date.now()) {
      localStorage.removeItem('access_token');
      return false;
    }
    return true;
  } catch (error) {
    return false;
  }
};
