import React, { useState, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import styled from 'styled-components';
/* import Form from './Form';
 */
import {
  Alert,
  AlertIcon,
  Button,
  FormControl,
  FormLabel,
  FormErrorMessage,
  Input,
} from '@chakra-ui/core';
import { create } from '../utils/receiptService';
import { upload } from '../utils/imageService';
import { sendImage } from '../utils/machineLearningService';

const Upload = () => {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);
  const [pictureIsSentError, setPictureIsSentError] = useState(false);
  const [pictureIsUploadedError, setPictureIsUploadedError] = useState(false);
  const [receiptError, setReceiptError] = useState(false);
  const [receiptSuccess, setReceiptSuccess] = useState(false);
  const [imageId, setImageId] = useState(null);
  const [receiptValue, setReceiptValue] = useState(null);
  const [src, setSrc] = useState(null);
  const [pictureIsSent, setPictureIsSent] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const { register, handleSubmit, formState, reset, errors } = useForm({
    mode: 'onBlur',
  });

  const onSubmit = async (formData) => {
    setIsLoading(true);
    console.log('Lagrer receipt');
    const data = await create(formData, imageId);
    console.log(data);
    if (data?.status === 201) {
      setReceiptSuccess(true);
      setIsLoading(false);
      setReceiptError(false);
    } else {
      setReceiptSuccess(false);
      setReceiptError(true);
      setIsLoading(false);
      setError(data?.error);
    }
  };

  useEffect(() => {
    if (pictureIsSent) {
      const fetchData = async () => {
        setIsLoading(true);
        console.log('Laster opp bilde');
        const data = await upload(file);
        console.log(data);
        if (data?.status === 201) {
          setImageId(data.data.imageId);
          setIsLoading(false);
        } else {
          setIsLoading(false);
          setPictureIsUploadedError(false);
        }
      };
      fetchData();
    }
  }, [reset, pictureIsSent, file]);

  const handleImageSubmit = async (e) => {
    e.preventDefault();
    console.log('Sender inn bilde');
    setIsLoading(true);
    const data = await sendImage(file);
    console.log(data);
    if (data?.status === 200) {
      reset(data.data);
      setReceiptValue(data?.data);
      setPictureIsSent(true);
      setPictureIsSentError(false);
      setIsLoading(false);
    } else {
      setPictureIsSent(false);
      setPictureIsSentError(true);
      setIsLoading(false);
    }
  };
  function arrayBufferToBase64(buffer) {
    let binary = '';
    const bytes = [].slice.call(new Uint8Array(buffer));
    bytes.forEach((b) => (binary += String.fromCharCode(b)));
    return window.btoa(binary);
  }

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
      {receiptSuccess && (
        <Alert status="success">
          <AlertIcon />
          {receiptValue.type}en har blitt lastet opp
        </Alert>
      )}
      {isLoading && <div>Laster opp...</div>}
      {(pictureIsUploadedError || pictureIsSentError || receiptError) && (
        <Alert status="error">
          <AlertIcon />
          Det har oppstått en feil, prøv igjen senere.
        </Alert>
      )}
      <FlexBox>
        <FlexStart>
          <FormGroup>
            <StyledForm onSubmit={handleSubmit(onSubmit)}>
              <FormControl isInvalid={errors.type}>
                <FormLabel htmlFor="inpType">Type</FormLabel>
                <Input
                  type="text"
                  name="type"
                  id="inpType"
                  placeholder="Type"
                  ref={register({
                    required: true,
                  })}
                />
                <FormErrorMessage valid={!errors.type}>
                  Fyll ut type
                </FormErrorMessage>
              </FormControl>
              <FormControl name="amount" isInvalid={errors.amount}>
                <InputLabel htmlFor="inpAmount">Pris</InputLabel>
                <Input
                  type="text"
                  name="amount"
                  id="inpAmount"
                  placeholder="Pris"
                  ref={register({
                    required: true,
                  })}
                />
                <FormErrorMessage valid={!errors.amount}>
                  Fyll ut pris
                </FormErrorMessage>
              </FormControl>
              <FormControl isInvalid={errors.company}>
                <InputLabel htmlFor="inpCompany">Selskap</InputLabel>
                <Input
                  type="text"
                  name="company"
                  id="inpCompany"
                  placeholder="Selskap"
                  ref={register({
                    required: true,
                  })}
                />
                <FormErrorMessage valid={!errors.company}>
                  Fyll ut selskap
                </FormErrorMessage>
              </FormControl>
              <FormControl isInvalid={errors.date}>
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
                <FormErrorMessage valid={!errors.date}>
                  Fyll ut dato
                </FormErrorMessage>
              </FormControl>
              <FormControl>
                <Button type="submit" isLoading={formState.isSubmitting}>
                  Send inn
                </Button>
                {error && <p>{error.message}</p>}
              </FormControl>
            </StyledForm>
          </FormGroup>
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

/* const SuccessMessage = styled.p`
  margin: 0;
  align-items: left;
`; */

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

/* const Input = styled.input`
  border-bottom: solid 0.1rem black;
  margin: 0.2rem 0rem;
`; */

const StyledButton = styled.button`
  padding: 0.1rem 0.65rem;
  border: solid 0.1rem black;
  border-radius: 0.2rem;
  margin: 0.1rem 0;
`;

const InputLabel = styled.label``;
