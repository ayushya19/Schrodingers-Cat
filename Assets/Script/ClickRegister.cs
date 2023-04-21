using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class ClickRegister : MonoBehaviour
{

    public GameObject[] cylinders=new GameObject[4];
    public static int randomInteger;
    public Material redMaterial;
    public Animator cat;
    void Start()
    {
        randomInteger= Random.Range(1, 5);
        randomInteger--;
        Debug.Log(randomInteger);
    }
    private void OnMouseDown()
    {
        foreach(GameObject cyl in cylinders)
        {
            cyl.SetActive(false);
        }
        this.gameObject.SetActive(true);
        int index = 0;
        foreach (GameObject cyl in cylinders)
        {
            if(cyl.gameObject.activeSelf == true)
            {
                if(index==randomInteger)
                {
                    Debug.Log(randomInteger);
                    Debug.Log("True");
                    cat.Play("Jump");
                    
                    
                }
                else
                {
                    this.gameObject.GetComponent<MeshRenderer>().material = redMaterial;
                }
            }
            index++;
        }

    }
}
