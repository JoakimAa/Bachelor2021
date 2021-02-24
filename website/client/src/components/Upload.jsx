import React, { useState, useEffect } from 'react';
import { useForm } from 'react-hook-form';

import styled from 'styled-components';
/* import Form from './Form';
 */
import { create, get } from '../utils/receiptService';
import { upload } from '../utils/imageService';

const Upload = () => {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const [imageId, setImageId] = useState(null);
  const [receiptValue, setReceiptValue] = useState(null);
  const [imageData, setImageData] = useState(null);
  const [src, setSrc] = useState(null);

  const { register, handleSubmit, formState, reset } = useForm({
    mode: 'onBlur',
  });

  function arrayBufferToBase64(buffer) {
    let binary = '';
    const bytes = [].slice.call(new Uint8Array(buffer));
    bytes.forEach((b) => (binary += String.fromCharCode(b)));
    return window.btoa(binary);
  }

  const onSubmit = async (formData) => {
    const { data } = await create(formData, { image: imageData._id });
    if (!data.success) {
      setError(data.message);
    } else {
      setSuccess(true);
      setError(null);
    }
  };

  useEffect(() => {
    if (src) {
      const fetchData = async () => {
        console.log('Running tempdata');
        /* setTempReceiptValue(await get(1).data.data); */
        const { data } = await get(2);
        /* setReceiptValue(await get(1)); */
        /* const { data } = await {
          data: {
            data: {
              type: 'Kvittering',
              amount: '200',
              date: '20.01.2021',
            },
            success: true,
          },
        }; */
        // reset(data.data);
        if (!data.success) {
          setError(data.error);
        } else {
          setReceiptValue(data?.data);
        }
      };
      fetchData();
    }
  }, [reset, src]);

  const handleImageSubmit = async (e) => {
    e.preventDefault();
    console.log('Laster opp bilde');
    const { data } = await upload();
    /* tempData(); */
    if (!data.success) {
      setError(data.message);
    } else {
      setImageData(data?.data);
      setImageId(data?.data?._id);
      setSuccess(true);
      setError(null);
    }
  };

  useEffect(() => {
    if (file) {
      const fetchData = async () => {
        const img = await file.arrayBuffer().then((buffer) => {
          const base64Flag = 'data:image/jpeg;base64,';
          const imageStr = arrayBufferToBase64(buffer);
          return base64Flag + imageStr;
        });
        setSrc(img);
      };
      fetchData();
    }
  }, [file]);

  return (
    <>
      {error && <p>Noe gikk galt med opplastingen</p>}
      {success && <p>Laster opp bilde med id: {imageId}</p>}
      <FlexBox>
        <FlexStart>
          {receiptValue && (
            <FormGroup>
              <StyledForm onSubmit={handleSubmit(onSubmit)}>
                <FormGroup>
                  <InputLabel htmlFor="inpType">Type</InputLabel>
                  <Input
                    type="text"
                    name="type"
                    id="inpType"
                    placeholder="Type"
                    ref={register({
                      required: true,
                    })}
                  />
                </FormGroup>
                <FormGroup>
                  <InputLabel htmlFor="impAmount">Pris</InputLabel>
                  <Input
                    type="text"
                    name="amount"
                    id="impAmount"
                    placeholder="Pris"
                    ref={register({
                      required: true,
                    })}
                  />
                </FormGroup>
                <FormGroup>
                  <InputLabel htmlFor="inpDate">Dato</InputLabel>
                  <Input
                    type="text"
                    name="date"
                    id="inpDate"
                    placeholder="Date"
                    ref={register({
                      required: true,
                    })}
                  />
                </FormGroup>
                <FormGroup>
                  <StyledButton
                    type="submit"
                    isLoading={formState.isSubmitting}
                  >
                    Send inn
                  </StyledButton>
                  {error && <p>{error.message}</p>}
                </FormGroup>
              </StyledForm>
            </FormGroup>
          )}

          {receiptValue && console.log(`True: ${receiptValue}`)}
          {console.log(`Just a log: ${receiptValue}`)}

          <StyledForm
            encType="multipart/form-data"
            method="post"
            onSubmit={handleImageSubmit}
          >
            <FormGroup>
              <FlexBoxImage>
                <Label htmlFor="image">Last opp bilde</Label>
                <FileInput
                  type="file"
                  id="image"
                  name="image"
                  accept=".jpg"
                  onChange={(event) => {
                    const imageFile = event.target.files[0];
                    setFile(imageFile);
                  }}
                />
                <StyledButton type="submit">Lagre</StyledButton>
              </FlexBoxImage>
            </FormGroup>
          </StyledForm>
        </FlexStart>
        {src && <Img alt="bilde" src={src} />}
      </FlexBox>
    </>
  );
};

export default Upload;

const FlexBox = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const FlexStart = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
`;

const FlexBoxImage = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: auto;
`;

const Label = styled.label``;

const FileInput = styled.input``;

const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
`;

const StyledForm = styled.form`
  margin: 1.5rem;
`;

const Img = styled.img`
  margin-top: 1rem;
  width: 50%;
  margin: auto;
`;

const Input = styled.input`
  border-bottom: solid 0.1rem black;
  margin: 0.2rem 0rem;
`;

const StyledButton = styled.button`
  padding: 0.1rem 0.65rem;
  border: solid 0.1rem black;
  border-radius: 0.2rem;
  margin: 0.1rem 0;
`;

const InputLabel = styled.label``;
