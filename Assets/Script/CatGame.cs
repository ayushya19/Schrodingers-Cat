using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CatGame : MonoBehaviour

{
    public GameObject[] _Startpages;
    int objectIndex = 0;
    public GameObject _panel;
    public GameObject box_1;
    //public GameObject box_2;
    public GameObject catAlive;
    public GameObject catDead;
    public GameObject homeIcon;
    public GameObject pressKeyButton;
    public GameObject mainCamera;
    public GameObject boxCamera;

    private bool isCatAlive = true;

    void Start()
    {
        _panel.SetActive(true);
        _Startpages[0].SetActive(true);
        _Startpages[1].SetActive(false);
        _Startpages[2].SetActive(false);

        Button pressKey = pressKeyButton.GetComponent<Button>();
        pressKey.onClick.AddListener(OnPressKeyButtonClick);

        Button home = homeIcon.GetComponent<Button>();
        home.onClick.AddListener(OnHomeIconClick);
    }
    public void OnClick()
    {
        objectIndex++;
        if (objectIndex >= _Startpages.Length)
        {
            _panel.SetActive(false);
            BoxShow();
            objectIndex = 0;
        }
        for (int i = 0; i < _Startpages.Length; i++)
        {
            if (i == objectIndex)
            {
                _Startpages[i].SetActive(true);
            }
            else
            {
                _Startpages[i].SetActive(false);

            }
        }
    }
    public void BoxShow()
    {
        box_1.SetActive(true);
        catAlive.SetActive(false);
        catDead.SetActive(false);
        homeIcon.SetActive(false);
        
    }
    void OnPressKeyButtonClick()
    {
        int random = Random.Range(0, 2);

        isCatAlive = (random == 0);

        if (isCatAlive)
        {
            catAlive.SetActive(true);
            catDead.SetActive(false);
        }
        else
        {
            catAlive.SetActive(false);
            catDead.SetActive(true);
        }

        //box_2.SetActive(true);
        //box_1.SetActive(false);

        homeIcon.SetActive(true);
        pressKeyButton.SetActive(false);


        mainCamera.SetActive(false);
        boxCamera.SetActive(true);
    }

    void OnHomeIconClick()
    {

        catAlive.SetActive(false);
        catDead.SetActive(false);

        homeIcon.SetActive(false);
        pressKeyButton.SetActive(true);

       // box_2.SetActive(false);
        //box_1.SetActive(true);

        boxCamera.SetActive(false);
        mainCamera.SetActive(true);
    }
}



