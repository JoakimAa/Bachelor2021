import http from './http';

const API_URL = '/machinelearning';

// export const createml = async (data) => {
//   try {
//     return await http.post(`${API_URL}`, data);
//   } catch (err) {
//     return err.response;
//   }
// };

export const sendImage = async (image) => {
  try {
    const data = new FormData();
    data.append('image', image);
    data.append('fileName', image.name);
    return await http.post(`${API_URL}`, data, {
      headers: { Accept: 'application/json' },
    });
  } catch (err) {
    return err.response;
  }
};

export default {
  sendImage,
};
